from django.shortcuts import render

# Create your views here.


def polls_testing(request):
    logger.warning('---- 2 ----')
    return render(request, 'polls_testing.html', {
        'data' : "Vote",
        })
