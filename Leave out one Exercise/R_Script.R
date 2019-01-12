#importing the anscombe dataset
data = read.csv(file="anscombe.csv",header=TRUE,sep=",")

#creating an empty matriz to store the slopes
box = matrix(0,11,4)

#getting slope
for(i in 1:4){
  for (j in 1:length(data$id)){
    anscombe = data[-j,2*i+1]
    anscombe_1 = data[-j,2*i]
    model = lm(anscombe~anscombe_1)
    box[j,i] = model$coefficients['anscombe_1']

  }
}  

#melt the matrix into list
library('reshape2')
melt_df = melt(box)
head(melt_df)

#imputing na to zero
melt_df$value[is.na(melt_df$value)] <- 0

#plotting
plot(x = as.integer(melt_df$Var2), y = melt_df$value, col = c("orangered4", "chartreuse4", "orange", 'azure4')[melt_df$Var2],  pch = 19, ylim=c(0, 0.7), xlim = c(0,4), ,xaxt = 'n', xlab = 'Dataset', ylab = 'SLR Slope Coefficient', main = 'Distribution of Leave-out SLR Slope Coefficients')
axis(1, at = 1:4)
#line segment at y = 0.5
segments(0,0.5,4,0.5, col = 'blue')

