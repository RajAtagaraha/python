# python
Python Projects

1. What is flask?
    
        Framework to develop lightweight web application 
        Based on WSGI toolkit and jinja template 

2. What is route decorator?
        
        It is used to route web page directly without visiting the home page. It binds url to a 
        function. 
         
        @app.route('/hello)
        def hello():
            return 'hello' 

3. How to add arguments in an url?
    
        Thrugh variable in the route rule
        
        Example 
        
        @app.route('/user/<username>')
        def get_url_user(username):
            return "The user :  %s" % username                     
 
4. 
