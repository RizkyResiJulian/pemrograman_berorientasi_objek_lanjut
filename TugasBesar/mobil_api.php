<?php
require_once 'database.php';
require_once 'Mobil.php';
$db = new MySQLDatabase();
$mobil = new Mobil($db);
$id=0;
$plat=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['plat'])){
            $plat = $_GET['plat'];
        }
        if($id>0){    
            $result = $mobil->get_by_id($id);
        }elseif($plat>0){
            $result = $mobil->get_by_plat($plat);
        } else {
            $result = $mobil->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new mobil
        $mobil->plat = $_POST['plat'];
        $mobil->merk = $_POST['merk'];
        $mobil->jenis = $_POST['jenis'];
        $mobil->warna = $_POST['warna'];
        $mobil->hargasewa = $_POST['hargasewa'];
       
        $mobil->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mobil created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mobil not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['plat'])){
            $plat = $_GET['plat'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $mobil->plat = $_PUT['plat'];
        $mobil->merk = $_PUT['merk'];
        $mobil->jenis = $_PUT['jenis'];
        $mobil->warna = $_PUT['warna'];
        $mobil->hargasewa = $_PUT['hargasewa'];
        if($id>0){    
            $mobil->update($id);
        }elseif($plat<>""){
            $mobil->update_by_plat($plat);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mobil updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mobil update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['plat'])){
            $plat = $_GET['plat'];
        }
        if($id>0){    
            $mobil->delete($id);
        }elseif($plat>0){
            $mobil->delete_by_plat($plat);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mobil deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mobil delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>