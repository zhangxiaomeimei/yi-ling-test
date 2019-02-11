from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/callback", methods=['POST'])

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Bisection Method Using Python</title>")
print("<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css\">")
print("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>")
print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js\"></script>")
print("<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js\"></script>")
print("</head>")
print("<body>")

print("<div class=\"container\">")
print("  <div class=\"jumbotron\">")
print("    <h1>Bootstrap Tutorial</h1>")      
print("    <p>Bootstrap is the most popular HTML, CSS, and JS framework for developing responsive, mobile-first projects on the web.</p>"
print("  </div>")
print("  <p>This is some text.</p>  ")    
print("  <p>This is another text.</p> ")     
print("</div>")

print("</body>")
print("</html>")