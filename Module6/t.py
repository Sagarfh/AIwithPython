# Step 1: Include the necessary modules for TensorFlow and the data set modules, which are needed to compute the CNN model.
import tensorflow as tf
# tf.disable_v2_behavior()
import numpy as np
import keras
import tensorflow_datasets
input_data = tensorflow_datasets.load('mnist')


# Step 2: Declare a function called run_cnn(), which includes various parameters and optimization variables with declaration of data placeholders. 
# These optimization variables will declare the training pattern.
def run_cnn():
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    learning_rate = 0.0001
    epochs = 10
    batch_size = 50

# Step 3: In this step, we will declare the training data placeholders with input parameters - for 28 x 28 pixels = 784. 
# This is the flattened image data that is drawn from mnist.train.nextbatch().
x = tf.keras.Input(tf.float32, [None, 784])
x_shaped = tf.reshape(x, [-1, 28, 28, 1])
y = tf.keras.Input(tf.float32, [None, 10])

# Step 4: Now it is important to create some convolutional layers:
def create_new_conv_layer(input_data, num_input_channels, num_filters, filter_shape, pool_shape, name):
    conv_filt_shape = [filter_shape[0], filter_shape[1], num_input_channels, num_filters]
    weights = tf.Variable(tf.truncated_normal(conv_filt_shape, stddev=0.03), name=name+'_W')
    bias = tf.Variable(tf.truncated_normal([num_filters]), name=name+'_b')
    #Out layer defines the output
    out_layer = tf.nn.conv2d(input_data, weights, [1, 1, 1, 1], padding='SAME')
    out_layer += bias
    out_layer = tf.nn.relu(out_layer)
    ksize = [1, pool_shape[0], pool_shape[1], 1]
    strides = [1, 2, 2, 1]
    out_layer = tf.nn.max_pool(out_layer, ksize=ksize, strides=strides, padding='SAME')
    return out_layer
    
layer1 = create_new_conv_layer(x_shaped, 1, 32, [5, 5], [2, 2], name='layer1')
layer2 = create_new_conv_layer(layer1, 32, 64, [5, 5], [2, 2], name='layer2')

# Step 5: Let us flatten the output ready for the fully connected output stage - after two layers of stride 2 pooling with the dimensions 
# of 28 x 28, to dimension of 14 x 14 or minimum 7 x 7 x,y co-ordinates, but with 64 output channels. To create the fully connected with 
# "dense" layer, the new shape needs to be [-1, 7 x 7 x 64]. We can set up some weights and bias values for this layer, then activate with ReLU.
flattened = tf.reshape(layer2, [-1, 7 * 7 * 64])
wd1 = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1000], stddev=0.03), name='wd1')
bd1 = tf.Variable(tf.truncated_normal([1000], stddev=0.01), name='bd1')
dense_layer1 = tf.matmul(flattened, wd1) + bd1
dense_layer1 = tf.nn.relu(dense_layer1)

# Step 6: Another layer with specific softmax activations with the required optimizer defines the accuracy assessment, 
# which makes the setup of initialization operator.
wd2 = tf.Variable(tf.truncated_normal([1000, 10], stddev=0.03), name='wd2')
bd2 = tf.Variable(tf.truncated_normal([10], stddev=0.01), name='bd2')
dense_layer2 = tf.matmul(dense_layer1, wd2) + bd2
y_ = tf.nn.softmax(dense_layer2)
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=dense_layer2, labels=y))
optimiser = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
init_op = tf.global_variables_initializer()

# Step 7: We should set up recording variables. This adds up a summary to store the accuracy of data.
tf.summary.scalar('accuracy', accuracy)
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('E:\TensorFlowProject')
with tf.Session() as sess:
    sess.run(init_op)
    total_batch = int(len(input_data.train.labels) / 50)
    for epoch in range(10):
        avg_cost = 0
        for i in range(total_batch):
            batch_x, batch_y = input_data.train.next_batch(batch_size=50)
            _, c = sess.run([optimiser, cross_entropy], feed_dict={x: batch_x, y: batch_y})
            avg_cost += c / total_batch
        test_acc = sess.run(accuracy, feed_dict={x: input_data.test.images, y: input_data.test.labels})
        summary = sess.run(merged, feed_dict={x: input_data.test.images, y: input_data.test.labels})
        writer.add_summary(summary, epoch)

        print("\nTraining complete!")
        writer.add_graph(sess.graph)
        print(sess.run(accuracy, feed_dict={x: input_data.test.images, y: input_data.test.labels}))



if __name__ == "__main__":
    run_cnn()