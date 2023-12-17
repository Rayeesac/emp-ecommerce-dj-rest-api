from django.shortcuts import render
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

from .serializers import *
from .models import *

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class OrderReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LineItem.objects.all()
    serializer_class = OrderReportRequestSerializer
        
    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")

    def create(self, request, *args, **kwargs):
        self.queryset = LineItem.objects.all()
        serializer = OrderReportRequestSerializer(data=request.data)

        if serializer.is_valid():
            skus = serializer.validated_data.get('skus', [])
            start_date = end_date = ''
            if 'date_range' in serializer.validated_data and serializer.validated_data['date_range']:
                start_date = serializer.validated_data['date_range']['start']
                end_date = serializer.validated_data['date_range']['end']
            
            lineitems = LineItem.objects

            if start_date and end_date:
                lineitems = lineitems.filter(
                    order__datetime__range=[start_date, end_date],
                )

            if skus: 
                lineitems = lineitems.filter(product__sku__in=skus)

            self.queryset = lineitems

            lineitems = lineitems.values('order__datetime', 'product__sku').annotate(
                sold_quantity=Sum('quantity')
            ).order_by('order__datetime', 'product__sku')

            result_data = []
            for row in lineitems:
                date = row['order__datetime'].strftime("%Y-%m-%d")
                product_data = {
                    "product" : row['product__sku'],
                    "sold_quantity": row['sold_quantity'],
                }

                # Check if the date is already present in the result_data
                date_entry = next((entry for entry in result_data if entry['date'] == date), None)
                if date_entry:
                    date_entry['data'].append(product_data)
                else:
                    result_data.append({
                        "date": date,
                        "data": [product_data],
                    })

            # Calculate total
            total_data = {"date": "Total", "data": []}
            for date_data in result_data:
                for product_data in date_data['data']:
                    existing_product = next(
                        (p for p in total_data['data'] if p['product'] == product_data['product']),
                        None,
                    )
                    if existing_product:
                        existing_product['sold_quantity'] += product_data['sold_quantity']
                    else:
                        total_data['data'].append(product_data)

            # Add the total entry
            result_data.append(total_data)

            return Response(result_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)