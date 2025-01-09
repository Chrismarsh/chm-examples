library(maptools) # also loads sp package
library(ncdf4)
library(raster)
library(rasterVis)
library(zoo)
library(gridExtra)
library(ggplot2)

obs <- raster('DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT/M3_LiDAR_Processed_2m_NAD83_UTM8N_TUPSR50DRIFT_projected.tif')
obs[ obs > 1]<-1

model <- raster('output/tvc136551_snowdepthavg2x2.tif')
model<-extend(model,obs)
model[ is.na(model)]<-0
model[ model > 1]<-1

z <- raster('DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT/DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT_projected.tif')
z<-setMinMax(z)
s<-stack(model,obs)

# # colr <- colorRampPalette(brewer.pal(9, 'viridis')) #col.regions=colr,
# ctour10<-contourplot(z,
#                      at = round(seq(minValue(z),maxValue(z),by=10)),
#                      margin=F,
#                      col='darkgray',
#                      labels=FALSE,
#                      scales=list(x=list(cex=1.3),y=list(cex=1.3))
# )
# ctour25<-contourplot(z,
#                      at = round(seq(minValue(z),maxValue(z),by=35)),
#                      margin=F,
#                      labels=F,
#                      col='black',
#                      scales=list(x=list(cex=1.3),y=list(cex=1.3))
# )

p<-levelplot(model,
             par.settings = viridisTheme,
             # col.regions=colr,
             colorkey=list(labels=list(cex=1, font=2, col="black",
                                       at=seq(0,1,0.1),
                                       labels= s),
                           height=.5, width=1.4,
                           title='Hs (m)', row=3, column=1, vjust=2, space="bottom"
             ),
             names.attr=c('PBSM3D'),
             margin=F,
             layout=c(2,1),
             at=seq(min(0), max(1), length.out=100),
             # scales=list(labels = XY.labels)
             scales=list(x=list(cex=1.3),y=list(cex=1.3))
)
# show(p)#+ctour10+ctour25)

#convert to gg grob thinger
plot_handle<-do.call(arrangeGrob,c(list(p),ncol=1,nrow=1)) 

ggsave('tvc.png',plot_handle,width=15)#,width=15)

