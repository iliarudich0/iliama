<!DOCTYPE html> 
<html>
<head>
    <title>Script</title>

    <script tpype="text/javascript">
        function myFunction() {
            alert("Hello! I am an alert box!");
        }
    </script>   


</head> 
<body>
    <h1>Script</h1>
    <button onclick="myFunction()">Click me</button>    
</body>
<hr>
<?php
    $variable = "Hello World!"; 
    echo "This is php - 1 $variable <br>";       
   
        ?>  
<?php
    echo "Hello World!";        
   
        ?>

<?php
     
$x= 5 /* + 15 */ + 5;   


$secretVariable = "password";
echo $x



   ?>
   <?php
    $x= 5;
    $y= 10;
    
    echo $x . $y;
   
        ?>
        
        <?php
        $mathIsGood = true  ;
        $mathIsBad = false ;

        if ($mathIsBad) {
            echo "Math is good";
        } else {
            echo "Math is bad";
        }
        ?>




</body>



</html>