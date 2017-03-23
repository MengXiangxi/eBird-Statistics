library(maps)
library(mapdata)
library(scales)
filename = "D:/ebird/20170212Swift/Adist.png"
png(file = filename, res = 600, width = 4800, height = 4800)
Dall<- read.csv("D:/ebird/20170212Swift/Swift_all.csv")
map("world", col="gray90", xlim=c(-30,135), ylim=c(-50,90), fill=TRUE)
points(Dall$lon, Dall$lat, pch=19, col=4, cex=0.25)
title(main = "eBird数据库中北京雨燕的记录分布", line = 0,
sub ="eBird Basic Dataset. Version: EBD_relAug-2015. Cornell Lab of Ornithology, Ithaca, New York. Aug 2015.",
cex.sub = 0.75)
mtext("Feb/11/2017 X.Meng", line = -1.25)
dev.off()