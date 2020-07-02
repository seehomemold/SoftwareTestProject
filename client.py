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
        time.sleep(0.1)
        result = RECEIVE()
        expected = "Register successfully. \r\n"
        #expected = "User name is already use.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')
    def test_registerForRepeatName(self):
        msg = "register Wing my-Email 123"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "User name is already use.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')
    def test_login(self):
        msg = "login Wing 123"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Welcome, Wing."
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')
    def test_loginRepeat(self):
        msg = "login Wing abc"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Please logout first.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_logout(self):
        msg = "logout"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Bye, Wing\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_logoutR(self):
        msg = "logout"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Please login first.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_loginWithWrongPass(self):
        msg = "login Wing 123456"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Login failed.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_loginWithWrongAcc(self):
        msg = "login hello 123"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Login failed.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_loginUsage(self):
        msg = "login 3"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Usage: login <username> <password>\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_registerUsage(self):
        msg = "register 3 3 3 3"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Usage: register <username> <email> <password>\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_whoami(self):
        msg = "whoami"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Please login first.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_whoamiAfterLogin(self):
        msg = "login Wing 123"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "whoami"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Wing\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_createboard(self):
        msg = "create-board S"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Create board successfully.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_createboard1(self):
        msg = "create-board S"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Board already exist.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_listboard(self):
        msg = "list-board"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE().split()[0]
        expected = "Index"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_listboard1(self):
        msg = "list-board ##S"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE().split()[0]
        expected = "Index"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_createP(self):
        msg = "create-post S --title A --content B"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Create post successfully."
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_listP(self):
        msg = "list-post S"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE().split()[0]
        expected = "ID"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_listP1(self):
        msg = "list-post S ##A"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE().split()[0]
        expected = "ID"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_listP2(self):
        msg = "list-post None"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Board does not exit."
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_listP3(self):
        msg = "list-post None ##12345"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Board does not exit."
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_read(self):
        msg = "read 1"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE().split()[0]
        expected = "Author"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_deleteP(self):
        msg = "delete-post 999"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Post does not exist."
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_deleteP1(self):
        msg = "delete-post 1"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "Delete successfully."
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_MixTest(self):
        msg = "create-post S --title second --content"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "update-post 2 --title We_update"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "update-post 2 --content We update content."
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "update-post 999 --content 123"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "update-post 9999 --title 123"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "comment 999 I comment"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "comment 2 I actually comment"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "list-post None ##12345"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "comment 2 I actually comment twice."
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "logout"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "create-board 12345"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "exit 1234567654"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "create-post S --title 123556 --content 333333"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "read 9999"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "delete-post 2"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "delete-post 12345876"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        msg = "update-post 2 --title he?"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()

        expected = "Please login first."
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')

    def test_(self):
        msg = "register b b b"
        SEND(CMD = msg)
        time.sleep(0.3)
        result = RECEIVE()
        expected = "User name is already use.\r\n"
        self.assertTrue(MatchOrNot(expected,result),'\r\nThe result :\r\n' + result + 'Is not match!')


Host = "18.204.221.141"
Port = 3110

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((Host,Port))
#print( RECEIVE())
targetBucket = None
userName = None

suite = unittest.TestSuite()
suite.addTest(ClientTestCase('test_connection'))
suite.addTest(ClientTestCase('test_wellcome'))
suite.addTest(ClientTestCase('test_register'))
suite.addTest(ClientTestCase('test_registerForRepeatName'))
suite.addTest(ClientTestCase('test_login'))
suite.addTest(ClientTestCase('test_loginRepeat'))
suite.addTest(ClientTestCase('test_logout'))
suite.addTest(ClientTestCase('test_logoutR'))
suite.addTest(ClientTestCase('test_loginWithWrongPass'))
suite.addTest(ClientTestCase('test_loginWithWrongAcc'))
suite.addTest(ClientTestCase('test_whoami'))
suite.addTest(ClientTestCase('test_whoamiAfterLogin'))
suite.addTest(ClientTestCase('test_createboard'))
suite.addTest(ClientTestCase('test_createboard1'))
suite.addTest(ClientTestCase('test_listboard'))
suite.addTest(ClientTestCase('test_listboard1'))
suite.addTest(ClientTestCase('test_createP'))
suite.addTest(ClientTestCase('test_listP'))
suite.addTest(ClientTestCase('test_listP1'))
suite.addTest(ClientTestCase('test_listP2'))
suite.addTest(ClientTestCase('test_listP3'))
suite.addTest(ClientTestCase('test_read'))
suite.addTest(ClientTestCase('test_deleteP'))
suite.addTest(ClientTestCase('test_deleteP1'))
suite.addTest(ClientTestCase('test_MixTest'))
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

