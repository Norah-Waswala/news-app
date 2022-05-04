from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
from app import views

# /* h1{
#     text-align: center;
#     color: red;
#     text-transform: capitalize;
#     font-weight: 400;
#     color: white
#   }
#   #head{
#     /* background-image: url("../images/cover.jpg");
#     background-position: center; */
#     /* background-attachment: fixed;
#     background-repeat: no-repeat;
#     background-size: cover;
#     text-align: center;
#     color: white;
#     font-weight: 400;
#     height: 50vh;
#   }
#   .overlay{
#     height: 50vh;
#     background-color: rgba(231, 6, 6, 0.329);
#     /* align-items: center;
#     text-align: center; */
#   /* }
#   img{
#     height: 200px;
#   }
#   h2{
#     text-align: center;
#     text-transform: capitalize;
#     color: #437C7B;
#   }
#   #title{
#     background-color: #437C7B;
#   }
#   #title:hover{
#     background-color: #9873;
#   }
#   .art{
#     text-align: center;
#     color: white;
#   }
#   .jumbo{
#     background-color: #588985 !important;
#   }
#   body{
#     background-color: #FBFCF9; */
#   /* }
#   .footer{
#     background-color:  rgba(231, 6, 6, 0.329)
#   }
#   @media screen  and (min-width:800px) {
#     #message{
#       position: absolute;
#       top: 150px;
#       left: 400px;
  
#     } */
#   /* }
#   span{
#     color: red;
#   } */ 
#   /* .top{
#     background-image: url("../images/bg.svg");
#     background-position: center;
#     background-attachment: fixed;
#     background-repeat: no-repeat;
#     background-size: cover;
#     font-weight: 400;
#     background-color: rgba(0,0,0,0.6);
#   }            */