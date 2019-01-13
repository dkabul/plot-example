from django.http import HttpResponse
import numpy as np

import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import io

import matplotlib.pyplot as plt, mpld3

def index(request):
#        n = np.array([2, 3, 4])
 #       name1 = "name-" + str(n[1])
  #      return HttpResponse('{ "name":"' + name1 + '", "age":31, "city":"New York" }')
    
    #fig = Figure()
    #canvas = FigureCanvas(fig)
    #x = np.arange(-2, 1.5, .01)
    #y = np.sin(np.exp(2 * x))
    #plt.plot(x, y)
    #buf = io.BytesIO()
    #plt.savefig(buf, format='png')
    #plt.close(fig)
    #response = django.http.HttpResponse(content_type='image/png')
    #canvas.print_png(response)
    #return response

    plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    mpld3.show()
