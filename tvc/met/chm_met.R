df <- read.table('siksik_1hrly_2012-2013.dat',header=T)
df$datetime <- as.POSIXct(paste(df$yr,df$mo,df$dy,df$hr), format="%Y %m %d %H ")
df$datetime<-format(df$datetime,format = '%Y%m%dT%H%M%S')
df <- df[c('datetime','tair','rh','wspd','wdir','prec')]
names(df) <- c('datetime','t','rh','u','vw_dir','p')

write.table(df,'siksik_1hr_chm_2012-2013.txt',sep="\t",quote=F,row.names=F)
