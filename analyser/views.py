import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Analysis
import matplotlib.pyplot as plt
import io
import urllib, base64

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            df = pd.read_csv(request.FILES['file'])
            # Perform data analysis
            analysis_result = df.describe()
            # Visualize data
            plt.plot(df['Date'], df['Cases'])
            plt.xlabel('Date')
            plt.ylabel('Cases')
            plt.title('COVID-19 Cases Over Time')
            # Save the plot as bytes
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            plt.close()
            # Convert bytes to base64 string
            analysis_plot = base64.b64encode(buffer.getvalue()).decode('utf-8')
            # Save analysis result and plot to the database
            analysis = Analysis(user=request.user, file=request.FILES['file'], analysis_result=analysis_result)
            analysis.save()
            return render(request, 'analysis_result.html', {'analysis': analysis, 'plot': analysis_plot})
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})