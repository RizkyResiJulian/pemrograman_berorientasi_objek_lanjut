SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `pelanggan` (
  `no` int(11) NOT NULL,
  `idpelanggan` int(5) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `jk` enum('L','P') NOT NULL DEFAULT 'L',
  `alamat` varchar(100) NOT NULL,
  `telp` char(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `pelanggan` (`no`,`idpelanggan`, `nama`, `jk`, `alamat`, `telp`) VALUES
(1, 29071, 'Budi Susanto', 'L', 'jln banjarwangunan','083213231312'),
(2, 29072, 'Sarah Wijanarko', 'P', 'jln watubelah','082434243322');

ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`no`),
  ADD UNIQUE KEY `idpelanggan` (`idpelanggan`);

ALTER TABLE `pelanggan`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;