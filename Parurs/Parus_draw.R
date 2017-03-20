library(maps)
library(mapdata)
library(scales)
png(file = "D:/ebird/20170211Parus/pdist.png", res = 600, width = 4800, height = 4800)
Dmajor<- read.csv("D:/eBird/20170211Parus/Pmajor.csv")
Dminor<- read.csv("D:/eBird/20170211Parus/Pminor.csv")
Dcinereus<- read.csv("D:/eBird/20170211Parus/Pcinereus.csv")
map("world", col="gray90", xlim=c(-20,150), ylim=c(-20,90), fill=TRUE)
points(Dmajor$lon, Dmajor$lat, pch=19, col=3, cex=0.25)
points(Dminor$lon, Dminor$lat, pch=19, col=2, cex=0.25)
points(Dcinereus$lon, Dcinereus$lat, pch=19, col=4, cex=0.25)
title(main = expression(paste("eBird数据库中", italic("Parus"), "属三种鸟的记录分布")), line = 0, 
sub ="eBird Basic Dataset. Version: EBD_relAug-2015. Cornell Lab of Ornithology, Ithaca, New York. Aug 2015.",
cex.sub = 0.75)
mtext("Feb/11/2017 X.Meng", line = -2)
legend(55, 2, 
       c(expression(italic("P. major")), 
         expression(paste(italic("P. minor"))), 
         expression(paste(italic("P. cinereus")))), 
       col = c(3, 2, 4), pch = 19, bg = "gray90")
dev.off()