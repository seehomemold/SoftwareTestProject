import socket
import os
import time
import datetime
import unittest

def RECEIVE():
    while True:
        try:
            msg_get = s.recv(1024).decode('utf-8')
            return msg_get
        except:
            pass

def SEND(CMD):
    while True:
        try:
            s.send(CMD.encode('utf-8'))
            break
        except:
            pass

def CmdLine():
    cmd = input("% ")
    test = cmd.replace(' ', '')
    while test == "":
        cmd = input("% ")
        test = cmd.replace(' ', '')
    SEND(CMD = cmd)
    return cmd

def MKDIR():
    Path = ".data"
    if not os.path.exists(Path):
        os.mkdir(Path)
    Ppost = ".data/post"
    Pcomment = ".data/comment"
    Pmail = ".data/mail"
    if not os.path.exists(Ppost):
        os.mkdir(Ppost)
    if not os.path.exists(Pcomment):
        os.mkdir(Pcomment)
    if not os.path.exists(Pmail):
        os.mkdir(Pmail)


def MatchOrNot(str1,str2):
    str1_clear = str1.replace("\r","").replace("\t","").replace("\n","")
    str2_clear = str2.replace("\r","").replace("\t","").replace("\n","")
    #print str1_clear
    #print str2_clear
    if(str1_clear == str2_clear):return True
    else: return False

class ClientTestCase(unittest.TestCase):
    def test_connection(self):
        global s
        s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.assertTrue(s)
        s.connect((Host,Port))
    def test_wellcome(self):
        result = RECEIVE()
        expected = "Welcome to the BBS !"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')
    def test_register(self):
        msg = "register Wing my-Email 123"
        SEND(CMD = msg)
        result = RECEIVE()
        expected = "Register successfully. \r\n"
        #expected = "User name is already use.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')


Host = "18.204.221.141"
Port = 3110

targetBucket = None
userName = None

suite = unittest.TestSuite()
suite.addTest(ClientTestCase('test_connection'))
suite.addTest(ClientTestCase('test_wellcome'))
suite.addTest(ClientTestCase('test_register'))
unittest.TextTestRunner(verbosity=2).run(suite)

msg = "exit"
SEND(CMD = msg)

#unittest.main()


##while True:
 ##   cmd = CmdLine();
    ##if cmd == "exit":
  ##      break
   ## else:
     ##   get = RECEIVE()
       ## print(get)

