setwd("~/Downloads")
dataset<-read.csv("glm_l_data.csv", header=TRUE)
x <- as.matrix(dataset)
datalist = list()

#if using total.csv, use i in 15:157
for (i in 16:158) {
  #lists the variable
  print(labels(dataset)[[2]][[i]])
  variable <- as.numeric(x[,i])
  name <- print(labels(dataset)[[2]][[i]])
  #linear regression model
  model <- glm(Group~variable+scan_age+factor(gender)+factor(race),family='binomial',data=dataset)
  #model <- lm(Braak_AB~variable+scan_age+time_last_path+factor(gender)+factor(race)+education,data=dataset)
  
  a <- summary(model)
  print(a)
  
  #finds effect size
  #e <- eta_squared(model)
  #print(e)
  
  #iteratively updates dataframe with model summaries
  #for using tidy(model)
    #dat <- data.frame(matrix(ncol = 0, nrow = 7), "variable" = c(name))
    #dat$i <- tidy(model)
  #for using eta_squared(model)
    #dat <- matrix(ncol = 0, nrow = 5)
    #dat$i <- cohens_d(model)
  #datalist[[i]] <- dat
  
  #plots model
  ggPredict(model, se=TRUE, interactive=TRUE, digits=4)
  #data_grid <- modelbased::estimate_link(model)
  
 #ggplot(data_grid, aes(x = i, y = Predicted)) +
    #geom_ribbon(aes(ymin = CI_low, ymax = CI_high), alpha = 0.2) +
    #geom_line(color = "red", size = 1) + 
    #see::theme_modern()
}

#combines dataframes into one dataframe
#big_data = do.call(rbind, datalist)
#write.csv(big_data, "/Users/allisonbeers/Downloads/glm.csv")
