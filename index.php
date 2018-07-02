<!DOCTYPE html>
<html>
<head>
  <title>Upload your files</title>
</head>
<body>
  <form enctype="multipart/form-data" action="index.php" method="POST">
    <p>Upload your file</p>
    <input type="file" name="uploaded_file"></input><br />
    <input type="submit" value="Upload"></input>
  </form>

  <!-- El tipo de codificación de datos, enctype, DEBE especificarse como sigue -->
<form enctype="multipart/form-data" action="index.php" method="POST">
    <!-- MAX_FILE_SIZE debe preceder al campo de entrada del fichero -->
    <input type="hidden" name="MAX_FILE_SIZE" value="30000" />
    <!-- El nombre del elemento de entrada determina el nombre en el array $_FILES -->
    Enviar este fichero: <input name="fichero_usuario" type="file" />
    <input type="submit" value="Enviar fichero" />
</form>

</body>
</html>
<?PHP
  $dir_subida = '/var/www/html/uploads/';
  $fichero_subido = $dir_subida . basename($_FILES['fichero_usuario']['name']);
  
  if (move_uploaded_file($_FILES['fichero_usuario']['tmp_name'], $fichero_subido)) {
      echo "El fichero es válido y se subió con éxito.\n";
  } else {
      echo "¡Posible ataque de subida de ficheros!\n";
  }
  
  echo 'Más información de depuración:';
  print_r($_FILES);
  
?>