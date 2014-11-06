import os
import Queue
class homebrew_awk():

    filename = ""
    split_string = " " # like " ", "|\"
    split_char_list =[" ",]  

    line_list = []
    result_line_list = []


    def __init__(self, filename, q): # init, get and check and load file
        if os.path.exists("./" + filename):
            self.filename = filename
        else:
            error_string = "AWK: file %s nonexist" % (filename)
            print error_string
            raise NameError(error_string)
        print "AWK: processing:", self.filename
        self.q = q

        #input = open(self.filename,'r')
        #self.line_list = []
        #for line in input.readlines():
        #    self.line_list.append( line.strip() )
            #print "AWK: line: ", line.strip()
        #input.close()

#    def get_queue(self):
#        return self.q

    def set_split(self,split_string): # set split string

        if len(split_string) == 0:
            raise NameError("AWK: empty split_string is not allowed")
        self.split_string = split_string
        self.split_char_list = []
        for char in self.split_string:
            self.split_char_list.append(char)
            print '''AWK: split char "%s" added''' % (char)
        #split it!
        
        self.result_line_list = []
        pre_result_list = []
        curr_result_list = []

        input = open(self.filename,'r')
        self.line_list = []
        for line in input.readlines():
            #self.line_list.append( line.strip() )
            #print "AWK: line: ", line.strip()

        #for line in self.line_list:
            line = line.strip()
            pre_result_list = []
            curr_result_list = [line]
            for char in self.split_char_list:
                pre_result_list = list(curr_result_list)
                curr_result_list = list()
                for sub_line in pre_result_list:
                    for piece in sub_line.split(char):
                      curr_result_list.append(piece)
            self.q.put(curr_result_list)
            #print "q_put_done"
            #self.result_line_list.append(curr_result_list)
            #print "AWK: from : %s" % (line)
            #print "AWK:   to :", curr_result_list
        input.close()        
        self.q.put("END")
        
    def set_state_machine(self):
        pass

    def get_state_machine(self):
        pass
