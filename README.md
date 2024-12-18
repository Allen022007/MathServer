# Ex.05 Design a Website for Server Side Processing
## Date: 1.12.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 

## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

~~~

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Power Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        input[type="text"], input[type="button"] {
            width: calc(100% - 20px);
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        input[type="button"] {
            background-color: #007bff;
            color: white;
            cursor: pointer;
            border: none;
        }
        input[type="button"]:hover {
            background-color: #0056b3;
        }
        label {
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }
    </style>
    <script>
        function power() {
            var i = parseFloat(document.getElementById("i1").value);
            var r = parseFloat(document.getElementById("i2").value);
            if (!isNaN(i) && !isNaN(r)) {
                document.getElementById("i3").value = (i ** 2) * r;
            } else {
                document.getElementById("i3").value = "Invalid Input";
            }
        }
    </script>
</head>
<body>
    <form>
        <label for="i1">Intensity:</label>
        <input type="text" id="i1" placeholder="Enter intensity">
        
        <label for="i2">Resistance:</label>
        <input type="text" id="i2" placeholder="Enter resistance">
        
        <input type="button" value="Calculate Power" onclick="power()">
        
        <label for="i3">Power:</label>
        <input type="text" id="i3" readonly>
    </form>
</body>
</html>

~~~

## HOMEPAGE:

![alt text](output.png)

## RESULT:
The program for performing server side processing is completed successfully.
