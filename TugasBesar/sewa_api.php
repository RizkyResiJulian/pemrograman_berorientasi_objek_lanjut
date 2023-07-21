<?php
require_once 'database.php';
require_once 'Sewa.php';
$db = new MySQLDatabase();
$sewa = new Sewa($db);
$id=0;
$idsewa=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['idsewa'])){
            $idsewa = $_GET['idsewa'];
        }
        if($id>0){    
            $result = $sewa->get_by_id($id);
        }elseif($idsewa>0){
            $result = $sewa->get_by_idsewa($idsewa);
        } else {
            $result = $sewa->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new sewa
        $sewa->idsewa = $_POST['idsewa'];
        $sewa->idpelanggan = $_POST['idpelanggan'];
        $sewa->plat = $_POST['plat'];
        $sewa->tglsewa = $_POST['tglsewa'];
        $sewa->waktu = $_POST['waktu'];
        $sewa->tglkembali = $_POST['tglkembali'];
        $sewa->hargasewa = $_POST['hargasewa'];
        $sewa->totalbiaya = $_POST['totalbiaya'];
       
        $sewa->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Sewa created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Sewa not created.';
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
        if(isset($_GET['idsewa'])){
            $idsewa = $_GET['idsewa'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $sewa->idsewa = $_PUT['idsewa'];
        $sewa->idpelanggan = $_PUT['idpelanggan'];
        $sewa->plat = $_PUT['plat'];
        $sewa->tglsewa = $_PUT['tglsewa'];
        $sewa->waktu = $_PUT['waktu'];
        $sewa->tglkembali = $_PUT['tglkembali'];
        $sewa->hargasewa = $_PUT['hargasewa'];
        $sewa->totalbiaya = $_PUT['totalbiaya'];
        if($id>0){    
            $sewa->update($id);
        }elseif($idsewa<>""){
            $sewa->update_by_idsewa($idsewa);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Sewa updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Sewa update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['idsewa'])){
            $idsewa = $_GET['idsewa'];
        }
        if($id>0){    
            $sewa->delete($id);
        }elseif($idsewa>0){
            $sewa->delete_by_idsewa($idsewa);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Sewa deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Sewa delete failed.';
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