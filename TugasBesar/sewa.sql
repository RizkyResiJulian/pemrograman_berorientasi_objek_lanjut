SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `sewa` (
  `no` int(11) NOT NULL,
  `idsewa` int(5) NOT NULL,
  `idpelanggan` int(5) NOT NULL,
  `plat` varchar(9) NOT NULL,
  `tglsewa` varchar(100) NOT NULL,
  `waktu` int(2) NOT NULL,
  `tglkembali` varchar(100) NOT NULL,
  `hargasewa` int(15) NOT NULL,
  `totalbiaya` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `sewa` (`no`,`idsewa`, `idpelanggan`, `plat`, `tglsewa`,`waktu`,`tglkembali`,`hargasewa`, `totalbiaya`) VALUES
(1, 07291, 29072, 'E 1234 BV', '19/07/2023', '2', '21/07/2023', 600000, waktu * hargasewa),
(2, 07292, 29071, 'E 2345 RFP', '19/07/2023', '2','21/07/2023', 500000,  waktu * hargasewa);

ALTER TABLE `sewa`
  ADD PRIMARY KEY (`no`), 
  ADD UNIQUE KEY `idsewa` (`idsewa`);

ALTER TABLE `sewa`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;