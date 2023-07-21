<?php
//Simpanlah dengan nama file : Pelanggan.php
require_once 'database.php';
class Pelanggan 
{
    private $db;
    private $table = 'pelanggan';
    public $idpelanggan = "";
    public $nama = "";
    public $jk = "";
    public $alamat = "";
    public $telp = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_idpelanggan(int $idpelanggan)
    {
        $query = "SELECT * FROM $this->table WHERE idpelanggan = $idpelanggan";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`idpelanggan`,`nama`,`jk`,`alamat`,`telp`) VALUES ('$this->idpelanggan','$this->nama','$this->jk','$this->alamat','$this->telp')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET idpelanggan = '$this->idpelanggan', nama = '$this->nama', jk = '$this->jk', alamat = '$this->alamat', telp = '$this->telp' 
        WHERE no = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_idpelanggan($idpelanggan): int
    {
        $query = "UPDATE $this->table SET idpelanggan = '$this->idpelanggan', nama = '$this->nama', jk = '$this->jk', alamat = '$this->alamat', telp = '$this->telp' 
        WHERE idpelanggan = $idpelanggan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE no = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_idpelanggan($idpelanggan): int
    {
        $query = "DELETE FROM $this->table WHERE idpelanggan = $idpelanggan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>