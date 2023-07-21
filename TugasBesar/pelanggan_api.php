<?php
require_once 'database.php';
require_once 'Pelanggan.php';
$db = new MySQLDatabase();
$pelanggan = new Pelanggan($db);
$id=0;
$idpelanggan=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['idpelanggan'])){
            $idpelanggan = $_GET['idpelanggan'];
        }
        if($id>0){    
            $result = $pelanggan->get_by_id($id);
        }elseif($idpelanggan>0){
            $result = $pelanggan->get_by_idpelanggan($idpelanggan);
        } else {
            $result = $pelanggan->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pelanggan
        $pelanggan->idpelanggan = $_POST['idpelanggan'];
        $pelanggan->nama = $_POST['nama'];
        $pelanggan->jk = $_POST['jk'];
        $pelanggan->alamat = $_POST['alamat'];
        $pelanggan->telp = $_POST['telp'];
       
        $pelanggan->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pelanggan created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pelanggan not created.';
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
        if(isset($_GET['idpelanggan'])){
            $idpelanggan = $_GET['idpelanggan'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pelanggan->idpelanggan = $_PUT['idpelanggan'];
        $pelanggan->nama = $_PUT['nama'];
        $pelanggan->jk = $_PUT['jk'];
        $pelanggan->alamat = $_PUT['alamat'];
        $pelanggan->telp = $_PUT['telp'];
        if($id>0){    
            $pelanggan->update($id);
        }elseif($idpelanggan<>""){
            $pelanggan->update_by_idpelanggan($idpelanggan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pelanggan updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pelanggan update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['idpelanggan'])){
            $idpelanggan = $_GET['idpelanggan'];
        }
        if($id>0){    
            $pelanggan->delete($id);
        }elseif($idpelanggan>0){
            $pelanggan->delete_by_idpelanggan($idpelanggan);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pelanggan deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pelanggan delete failed.';
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