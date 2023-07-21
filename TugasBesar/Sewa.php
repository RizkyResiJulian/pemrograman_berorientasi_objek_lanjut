<?php
//Simpanlah dengan nama file : Sewa.php
require_once 'database.php';
class Sewa 
{
    private $db;
    private $table = 'sewa';
    public $idsewa = "";
    public $idpelanggan = "";
    public $plat = "";
    public $tglsewa = "";
    public $waktu = "";
    public $tglkembali = "";
    public $hargasewa = "";
    public $totalbiaya = "";
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
    public function get_by_idsewa(int $idsewa)
    {
        $query = "SELECT * FROM $this->table WHERE idsewa = $idsewa";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`idsewa`,`idpelanggan`,`plat`,`tglsewa`,`waktu`,`tglkembali`,`hargasewa`,`totalbiaya`) VALUES ('$this->idsewa','$this->idpelanggan','$this->plat','$this->tglsewa','$this->waktu','$this->tglkembali','$this->hargasewa','$this->totalbiaya')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET idsewa = '$this->idsewa', idpelanggan = '$this->idpelanggan', plat = '$this->plat', tglsewa = '$this->tglsewa', waktu = '$this->waktu', tglkembali = '$this->tglkembali', hargasewa = '$this->hargasewa', totalbiaya = '$this->totalbiaya' 
        WHERE no = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_idsewa($idsewa): int
    {
        $query = "UPDATE $this->table SET idsewa = '$this->idsewa', idpelanggan = '$this->idpelanggan', plat = '$this->plat', tglsewa = '$this->tglsewa', waktu = '$this->waktu', tglkembali = '$this->tglkembali', hargasewa = '$this->hargasewa', totalbiaya = '$this->totalbiaya' 
        WHERE idsewa = $idsewa";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE no = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_idsewa($idsewa): int
    {
        $query = "DELETE FROM $this->table WHERE idsewa = $idsewa";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>