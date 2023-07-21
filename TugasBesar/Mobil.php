<?php
//Simpanlah dengan nama file : Mobil.php
require_once 'database.php';
class Mobil 
{
    private $db;
    private $table = 'mobil';
    public $plat = "";
    public $merk = "";
    public $jenis = "";
    public $warna = "";
    public $hargasewa = "";
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
    public function get_by_plat(int $plat)
    {
        $query = "SELECT * FROM $this->table WHERE plat = $plat";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`plat`,`merk`,`jenis`,`warna`,`hargasewa`) VALUES ('$this->plat','$this->merk','$this->jenis','$this->warna','$this->hargasewa')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET plat = '$this->plat', merk = '$this->merk', jenis = '$this->jenis', warna = '$this->warna', hargasewa = '$this->hargasewa' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_plat($plat): int
    {
        $query = "UPDATE $this->table SET plat = '$this->plat', merk = '$this->merk', jenis = '$this->jenis', warna = '$this->warna', hargasewa = '$this->hargasewa' 
        WHERE plat = $plat";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_plat($plat): int
    {
        $query = "DELETE FROM $this->table WHERE plat = $plat";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>