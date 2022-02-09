# binary tree insertion

class Node :
    def __init__ ( self , data ) :
        self.left = None
        self.data = data
        self.right = None

class BinaryTree :
    def __init__ ( self ) : 
        self.root = None
        self.dllHead = None
        self.dllTail = None
    
    def insert ( self , data ) :
        if self.root == None :
            self.root = Node ( data )
            return
        
        temp = self.root
        q = [ temp ]
        index = 0
        while index != len ( q ) :
            
            if temp == None : 
                temp = Node ( data )
                return
        
            if temp.data == data : return # data exists
        
            if temp.left : q.append ( temp.left )
            else :
                temp.left = Node ( data )
                return
        
            if temp.right : q.append ( temp.right )
            else : 
                temp.right = Node ( data )
                return
            
            index += 1
            temp = q [ index ]
            
        print ( " something unfathomable happened! " )
        return

    def printList ( self , node ) :
        if node == None : return
        if node.data : print ( node.data ) #data exists
        if node.left : 
            print ( " --- L of" , node.data , ":")
            self.printList ( node.left )
        if node.right : 
            print ( " --- R of" , node.data )
            self.printList ( node.right )
        return
    
    def toDoublyLinkedList ( self , node ) :
        if node == None : return

        self.toDoublyLinkedList ( node.left )
         
        if self.dllHead == None : self.dllHead = node
        else:
            self.dllTail.right = node
            node.left = self.dllTail
        self.dllTail = node
         
        self.toDoublyLinkedList ( node.right )
        return
    
    def printDoublyLinkedList ( self ) :
        if self.dllHead == None : return
        temp = self.dllHead
        while temp :
            print ( temp.data )
            temp = temp.right
        return

Obj = BinaryTree ()
arr = [ 5 , 8 , 3 , 2 , 6 , 4 , 9 , 1 , 7 ]
for index , value in enumerate ( arr ) : Obj.insert ( value )

Obj.toDoublyLinkedList ( Obj.root )
Obj.printDoublyLinkedList ()
