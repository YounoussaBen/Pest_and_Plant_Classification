# Summary of Plant Disease Classifier

Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d_1 (Conv2D)           (None, 64, 64, 32)        896       
                                                                 
 activation_1 (Activation)   (None, 64, 64, 32)        0         
                                                                 
 batch_normalization_1 (Bat  (None, 64, 64, 32)        128       
 chNormalization)                                                
                                                                 
 max_pooling2d_1 (MaxPoolin  (None, 21, 21, 32)        0         
 g2D)                                                            
                                                                 
 dropout_1 (Dropout)         (None, 21, 21, 32)        0         
                                                                 
 conv2d_2 (Conv2D)           (None, 21, 21, 64)        18496     
                                                                 
 activation_2 (Activation)   (None, 21, 21, 64)        0         
                                                                 
 batch_normalization_2 (Bat  (None, 21, 21, 64)        256       
 chNormalization)                                                
                                                                 
 conv2d_3 (Conv2D)           (None, 21, 21, 64)        36928     
                                                                 
 activation_3 (Activation)   (None, 21, 21, 64)        0         
                                                                 
 batch_normalization_3 (Bat  (None, 21, 21, 64)        256       
 chNormalization)                                                
                                                                 
 max_pooling2d_2 (MaxPoolin  (None, 10, 10, 64)        0         
 g2D)                                                            
                                                                 
 dropout_2 (Dropout)         (None, 10, 10, 64)        0         
                                                                 
 conv2d_4 (Conv2D)           (None, 10, 10, 128)       73856     
                                                                 
 activation_4 (Activation)   (None, 10, 10, 128)       0         
                                                                 
 batch_normalization_4 (Bat  (None, 10, 10, 128)       512       
 chNormalization)                                                
                                                                 
 conv2d_5 (Conv2D)           (None, 10, 10, 128)       147584    
                                                                 
 activation_5 (Activation)   (None, 10, 10, 128)       0         
                                                                 
 batch_normalization_5 (Bat  (None, 10, 10, 128)       512       
 chNormalization)                                                
                                                                 
 max_pooling2d_3 (MaxPoolin  (None, 5, 5, 128)         0         
 g2D)                                                            
                                                                 
 dropout_3 (Dropout)         (None, 5, 5, 128)         0         
                                                                 
 flatten_1 (Flatten)         (None, 3200)              0         
                                                                 
 dense_1 (Dense)             (None, 1024)              3277824   
                                                                 
 activation_6 (Activation)   (None, 1024)              0         
                                                                 
 batch_normalization_6 (Bat  (None, 1024)              4096      
 chNormalization)                                                
                                                                 
 dropout_4 (Dropout)         (None, 1024)              0         
                                                                 
 dense_2 (Dense)             (None, 38)                38950     
                                                                 
 activation_7 (Activation)   (None, 38)                0         
                                                                 
=================================================================
Total params: 3600294 (13.73 MB)
Trainable params: 3597414 (13.72 MB)
Non-trainable params: 2880 (11.25 KB)
_________________________________________________________________




# Summary of Pest Classifier

Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 efficientnetb4 (Functional  (None, 1792)              17673823  
 )                                                               
                                                                 
 batch_normalization (Batch  (None, 1792)              7168      
 Normalization)                                                  
                                                                 
 dense (Dense)               (None, 100)               179300    
                                                                 
 batch_normalization_1 (Bat  (None, 100)               400       
 chNormalization)                                                
                                                                 
 dense_1 (Dense)             (None, 10)                1010      
                                                                 
 batch_normalization_2 (Bat  (None, 10)                40        
 chNormalization)                                                
                                                                 
 dense_2 (Dense)             (None, 12)                132       
                                                                 
=================================================================
Total params: 17861873 (68.14 MB)
Trainable params: 184246 (719.71 KB)
Non-trainable params: 17677627 (67.43 MB)
_________________________________________________________________