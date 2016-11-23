# About the recommender system of film. 
#mathod : 基于内存的协同过滤：用户-产品协同过滤。产品-产品协同过滤。
# coding: utf-8

# In[163]:

#我们将使用MovieLens数据集，它是在实现和测试推荐引擎时所使用的最常见的数据集之一。
#它包含来自于943个用户以及精选的1682部电影的100K个电影打分。你应该添加解压缩的movielens数据文件夹你的notebook目录下。
#你也可以在这里下载数据集。http://files.grouplens.org/datasets/movielens/
import numpy as np
import pandas as pd


# In[164]:

#读入u.data文件，它包含完整的数据集。你可以 file, which contains the full dataset. 
#You can在这里（http://files.grouplens.org/datasets/movielens/ml-100k-README.txt）阅读该数据集的简要说明。
header = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('ml-100k/u.data', sep='\t', names = header)


# In[165]:

#先看看数据集中的前两行。接下来，让我们计算唯一用户和电影的数量。
n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
print'Number of users = ' + str(n_users) + '| Number of movides = ' + str(n_items)


# In[166]:

#你可以使用scikit-learn库将数据集分割成测试和训练。Cross_validation.train_test_split
#根据测试样本的比例（test_size），本例中是0.25，来将数据混洗并分割成两个数据集。

from sklearn import cross_validation as cv
train_data, test_data = cv.train_test_split(df, test_size=0.25)


# In[167]:

#Create two user-item matrices, one for training and another for testing
#df.itertuples() : Iterate over DataFrame rows as namedtuples, with index value as first element of the tuple.
#如第一条数据：训练集上的第3列（打分3）放在训练矩阵的第195行第241列的位置
#train_data_matrix是所有用户对所有电影的打分的矩阵943*1682

train_data_matrix = np.zeros((n_users, n_items))
for line in train_data.itertuples():
    train_data_matrix[line[1]-1, line[2]-1] = line[3]


test_data_matrix = np.zeros((n_users, n_items))
for line in test_data.itertuples():
    test_data_matrix[line[1]-1, line[2]-1] = line[3]
#print train_data_matrix


# In[168]:

#使用sklearn的pairwise_distances函数来计算余弦相似性。注意，输出范围从0到1，因为打分都是正的。.T 转置

from sklearn.metrics.pairwise import pairwise_distances
user_similarity = pairwise_distances(train_data_matrix, metric = 'cosine')
item_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')


# In[169]:

#np.dot(a,b)用来计算数组的点积
#.dot()为点乘. axis = 1 对每一行求和，axis = 0 对每一列求和

def predict(ratings, similarity, type = 'user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis = 1)
        #You use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff)/ np.array([np.abs(similarity).sum(axis = 1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis = 1)])
    return pred

item_prediction = predict(train_data_matrix, item_similarity, type = 'item')
user_prediction = predict(train_data_matrix, user_similarity, type = 'user')


# In[170]:

from sklearn.metrics import mean_squared_error
from math import sqrt

def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

print 'User-based CF RMSE:' + str(rmse(user_prediction, test_data_matrix))
print 'Item-based CF RMSE:' + str(rmse(item_prediction, test_data_matrix))


# In[171]:

sparsity = round(1.0 - len(df)/float(n_users*n_items),5)
print 'The sparsity level of MovieLens100K is ' + str(sparsity*100) + '%'
