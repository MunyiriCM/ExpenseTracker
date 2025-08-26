from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    if response is not None:
        # If DRF already handled the exception, just format the response
        return Response({
            "error": True,
            "status_code": response.status_code,
            "message": response.data
        }, status=response.status_code)

    # Handle unhandled exceptions (server errors, etc.)
    return Response({
        "error": True,
        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
        "message": "An unexpected error occurred. Please try again later."
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
