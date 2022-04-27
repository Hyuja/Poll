from django.shortcuts import redirect, render
import os
from urllib import parse
from .models import *
from userapp.models import *
from plotly.offline import plot
from plotly import graph_objects as go 
from matplotlib import pyplot as plt
import random

def menu (request):
    return render (request, "menu.html")
#===================================================
def CandidateEdit(request):
    Candidates = Candidate.objects.all()
    return render (request, "CandidateEdit.html", {'Candidates' : Candidates})

def PollResult(request):
    if request.user.is_authenticated and request.user.is_staff:
        POLL_CASES = Poll_Cases.objects.all().order_by('poll_case_num')
        Candidates = Candidate.objects.all().order_by('Poll_Case_id')
        
        alllst = Candidate.objects.filter(id = -1)
        for pollcase in POLL_CASES:
            canlst = Candidate.objects.filter(id = -1)
            canlst = canlst | Candidate.objects.filter(Poll_Case_id = pollcase.id).order_by('-votes')       #votes 올림차순. canlst[0]이 최다득표임 
            alllst = alllst | canlst
        return render (request, "PollResult.html", {"POLL_CASES" : POLL_CASES, "alllst" : alllst})
    else:
        return redirect ('accessdenied')

def chart(request, id):
    pollcase = Poll_Cases.objects.filter(id = id)
    can = Candidate.objects.filter(Poll_Case_id = pollcase[0].id).order_by('-votes')
    
    colors = []
    for ca in can:
        colors.append(ca.CandidateColor)
    
    #======================================================================================
    
    ##PIE CHART
    labels = []
    values = []
    for ca in can:
        labels.append(str(ca.side) + (" ") + str(ca.CandidateName))
        values.append(int(ca.votes))
    
    
    piechart = go.Figure(data = [go.Pie(labels = labels, values = values, marker_colors = colors)])
    piechart = plot({'data' : piechart}, output_type = 'div')

    
    #======================================================================================

    ##HORIZIONTAL BAR CHARTS
    top_labels = labels

    y_data = ['70대 이상', '60대', '50대', '40대', '30대', '20대<br>10대 포함']     #fiexed field
    
    x_data = [[21, 30, 21, 16, 12],
            [24, 31, 19, 15, 11],
            [27, 26, 23, 11, 13],
            [29, 24, 15, 18, 14],
            [27, 26, 23, 11, 13],
            [27, 26, 23, 11, 13],
            [27, 26, 23, 11, 13],]


    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                marker=dict(
                    color=colors[i],
                    line=dict(color='rgb(248, 248, 249)', width=1)
                )
            ))

    fig.update_layout(
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            domain=[0.15, 1]
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode='stack',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=120, r=10, t=140, b=80),
        showlegend=False,
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0.14, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Arial', size=14,
                                        color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=14,
                                        color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the first Likert scale (on the top)
        if yd == y_data[-1]:
            annotations.append(dict(xref='x', yref='paper',
                                    x=xd[0] / 2, y=1.1,
                                    text=top_labels[0],
                                    font=dict(family='Arial', size=14,
                                            color='rgb(67, 67, 67)'),
                                    showarrow=False))
        space = xd[0]
        for i in range(1, len(xd)):
                # labeling the rest of percentages for each bar (x_axis)
                annotations.append(dict(xref='x', yref='y', x=space + (xd[i]/2), y=yd, text=str(xd[i]) + '%', font=dict(family='Arial', size=14, color='rgb(248, 248, 255)'),
                                        showarrow=False))
                # labeling the Likert scale
                if yd == y_data[-1]:
                    annotations.append(dict(xref='x', yref='paper',
                                            x=space + (xd[i]/2), y=1.1,
                                            text=top_labels[i],
                                            font=dict(family='Arial', size=14,
                                                    color='rgb(67, 67, 67)'),
                                            showarrow=False))
                space += xd[i]

    fig.update_layout(annotations=annotations)

    fig = plot({'data' : fig}, output_type = 'div')

    return render(request, 'chart.html', context = {'plot_div' : piechart, 'fig' : fig })


def accessdenied (request):
    return render (request, 'accessdenied.html')

