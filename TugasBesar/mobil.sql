SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `mobil` (
  `id` int(11) NOT NULL,
  `plat` varchar(9) NOT NULL,
  `merk` varchar(15) NOT NULL,
  `jenis` varchar(20) NOT NULL,
  `warna` varchar(15) NOT NULL,
  `hargasewa` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `mobil` (`id`,`plat`, `merk`, `jenis`,`warna`,`hargasewa`) VALUES
(1,'E 1234 BV', 'Honda', 'HRV','Merah',600000),
(2,'E 2345 RFP', 'Toyota', 'Avanza','Hitam',500000);

ALTER TABLE `mobil`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `plat` (`plat`);

ALTER TABLE `mobil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;