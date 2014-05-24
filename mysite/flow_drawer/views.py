# Create your views here.
from django.shortcuts import render, get_object_or_404
from flow_drawer.models import FlowDrawer
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import re

def index(request):
	signal_flow_code = []
        message_and_signal = []
        message = []
        signal = []
        network_element_all = ''
        network_element = ''
        space_add = ''
        line_one  = ''
        line_draw = []
        signal_flow = ''
        types = ''
        tmp = []
	tmp_message = ''
        direction_line = ''
        arrow_line = list()
        tmp_list_signal = list()
        list_signal = list()
        final_arrow_line = ''
        dict_line = dict()
        dict_arrow = dict()
        direction = ''
        if 'signal_flow_code' in request.POST:
                tmp = str(request.POST['signal_flow_code']).split('\r\n')
                network_element = tmp.pop(0).split('@')[1]
                message_and_signal = tmp

        list_network_element = network_element.split()
        final_line = network_element
        
        for i in list_network_element:
                line_draw.append(len(i)/2 * ' ' + '|' + (len(i)-len(i)/2-1)*' ')
                
        dict_line =dict(zip(list_network_element,line_draw))
        
        for i in range(len(dict_line.keys())):
                final_line = final_line.replace(dict_line.keys()[i],dict_line.values()[i],1)
                

        for context in message_and_signal:
                if '->' in context:
                        signal.append(context)
                        tmp_list_signal = signal[0].split('->')
                else:
                        message.append(context)


        if tmp_list_signal:
                if list_network_element.index(tmp_list_signal[0]) < list_network_element.index(tmp_list_signal[1]):
                        direction = 'forward'
                elif list_network_element.index(tmp_list_signal[0]) > list_network_element.index(tmp_list_signal[1]):
                        direction = 'backward'
                else:
                        direction = 'wrong'
                        
        final_arrow_line = final_line
        j = 0
        dict_arrow = dict_line.copy()

        if direction == 'forward':
                for item in tmp_list_signal:
                        for ne in dict_arrow.keys():
                                if item == ne :
                                        if  j == 0:
                                                list_signal.append(len(ne)/2 * ' ' + '|' + (len(ne)-len(ne)/2-1) * '-' );
                                        elif j == 1:
                                                list_signal.append((len(ne)/2-1) * '-' + '>' + '|' + (len(ne)-len(ne)/2-1) * ' ' );        
                        
                                        dict_arrow[ne] = list_signal[j]
                                        j = j +1
                d = list_signal
                final_arrow_line = network_element
                for element in dict_arrow.keys():
                        final_arrow_line = final_arrow_line.replace(element,dict_arrow[element],1)
                        final_arrow_line = re.sub("\-[\-\| ]*\>", lambda x:x.group(0).replace('|',' ').replace(' ','-'), final_arrow_line)
                                                
        elif direction == 'backward':
                for item in tmp_list_signal:
                        for ne in dict_arrow.keys():
                                if item == ne :
                                        if  j == 1:
                                                list_signal.append(len(ne)/2 * ' ' + '|' + '<' + (len(ne)-len(ne)/2-2) * '-' );
                                        elif j == 0:
                                                list_signal.append((len(ne)/2) * '-' + '|'  + (len(ne)-len(ne)/2-1) * '' );        
                                        dict_arrow[ne] = list_signal[j]
                                        j = j +1
                d = list_signal
                final_arrow_line = network_element
                for element in dict_arrow.keys():
                        final_arrow_line = final_arrow_line.replace(element,dict_arrow[element],1)
                        final_arrow_line = re.sub("\<[\-\| ]*\-", lambda x:x.group(0).replace('|',' ').replace(' ','-'), final_arrow_line)
        
        
        

	context ={'network_element': network_element,
                  'final_line': final_line,
                  'times': range(10),
                  'signal': signal,
                  'message': message,
                  'final_arrow_line': final_arrow_line,
                  'a': dict_line,
                  'c': tmp_list_signal,
                  'd': direction,
                  'b': dict_arrow
                 }


	return render(request, 'flow_drawer/index.html', context)
