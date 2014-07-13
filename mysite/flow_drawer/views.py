# Create your views here.
from django.shortcuts import render, get_object_or_404
from flow_drawer.models import FlowDrawer
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from collections import OrderedDict
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
        final_arrow_line = list()
        dict_line = dict()
        dict_arrow = dict()
        direction = list()
        try :
                if 'signal_flow_code' in request.POST:
                        tmp = str(request.POST['signal_flow_code']).split('\r\n')
                        network_element = tmp.pop(0).split('@')[1]
                        message_and_signal = tmp
        except :
                network_element = ''
                
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
                else:
                        message.append(context)
                        
        try :
                for item in range(len(message)) :
                        if not message[0] :
                                message.pop(0)
                        elif message[0] :
                                break
        except IndexError :
                message = []
        
                        
        for count in range(len(signal)):
                tmp_list_signal.append(signal[count].strip().split('->'))
        
        for signal_count in range(len(tmp_list_signal)):
                if tmp_list_signal[0]:
                        if list_network_element.index(tmp_list_signal[signal_count][0]) < list_network_element.index(tmp_list_signal[signal_count][1]):
                                direction.append('forward')
                        elif list_network_element.index(tmp_list_signal[signal_count][0]) > list_network_element.index(tmp_list_signal[signal_count][1]):
                                direction.append('backward')
                        else:
                                direction.append('wrong')
                        

        #Draw the arrow line

        for signal_count in range(len(tmp_list_signal)): 
                j = 0
                list_signal = list()
                dict_arrow = dict_line.copy()
                if direction[signal_count]== 'forward':
                        for item in tmp_list_signal[signal_count]:
                                for ne in dict_arrow.keys():
                                        if item == ne :
                                                if  j == 0:
                                                        list_signal.append(len(ne)/2 * ' ' + '|' + (len(ne)-len(ne)/2-1) * '-' )
                                                elif j == 1:
                                                        list_signal.append((len(ne)/2-1) * '-' + '>' + '|' + (len(ne)-len(ne)/2-1) * ' ' )
                                                dict_arrow[ne] = list_signal[j]
                                                j = j +1

                        d = list_signal
                        final_arrow_line.append(network_element)
                        for element in dict_arrow.keys():
                                final_arrow_line[signal_count] = final_arrow_line[signal_count].replace(element,dict_arrow[element],1)
                                final_arrow_line[signal_count] = re.sub("\-[\-\| ]*\>", lambda x:x.group(0).replace('|',' ').replace(' ','-'), final_arrow_line[signal_count])
                                                
                elif direction[signal_count] == 'backward':
                        for item in tmp_list_signal[signal_count]:
                                for ne in dict_arrow.keys():
                                        if item == ne :
                                                if  j == 1:
                                                        list_signal.append(len(ne)/2 * ' ' + '|' + '<' + (len(ne)-len(ne)/2-2) * '-' )
                                                elif j == 0:
                                                        list_signal.append((len(ne)/2) * '-' + '|'  + (len(ne)-len(ne)/2-1) * ' ' )
                                                dict_arrow[ne] = list_signal[j]
                                                j = j +1
                        d = list_signal
                        final_arrow_line.append(network_element)
                        for element in dict_arrow.keys():
                                final_arrow_line[signal_count] = final_arrow_line[signal_count].replace(element,dict_arrow[element],1)
                                final_arrow_line[signal_count] = re.sub("\<[\-\| ]*\-", lambda x:x.group(0).replace('|',' ').replace(' ','-'), final_arrow_line[signal_count])

        # Draw arrow line end

        message_count = 0
        list_all_context = list()
        k = 0
        arrow_count = 0
        for arrow_count in range(len(final_arrow_line)):
                if final_arrow_line[arrow_count]:
                        list_all_context.append(final_arrow_line[arrow_count])
                try :
                        while message[message_count] :
                                list_all_context.append(message[message_count])
                                message_count = message_count +1
                except IndexError:
                        break
                
                message_count= message_count + 1
                list_all_context.append(final_line)

        message_count = 0
        dict_all_context = OrderedDict()
        list_all_context_value = []
        
        for arrow_count in range(len(final_arrow_line)):
                if final_arrow_line[arrow_count]:
                        try :
                                while message[message_count] :
                                        list_all_context_value.append(message[message_count])
                                        message_count = message_count + 1
                        except IndexError:
                                break

                        message_count= message_count + 1
                        list_all_context_value.append(final_line)
                        dict_all_context[final_arrow_line[arrow_count]] = list(list_all_context_value)  #should use a = list(b) instead of a = b ,as the second will make a equals b all the time.
                        list_all_context_value = list()


                                 
        

	context ={'network_element': network_element,
                  'final_line': final_line,
                  'times': range(10),
                  'message': message,
                  'final_arrow_line': final_arrow_line,
                  'a': dict_line,
                  'c': tmp_list_signal,
                  'd': 'kk',
                  'b': dict_arrow,
                  'list_all_context': list_all_context,
                  'list_all_context_value': list_all_context_value,
                  'message_count' : message_count,
                  'arrow_count' : arrow_count,
                  'dict_all_context_values' : dict_all_context.values(),
                  'dict_all_context_keys' : dict_all_context.keys(),
                  'dict_all_context' : dict_all_context.items()
                 }



	return render(request, 'flow_drawer/index.html', context)
