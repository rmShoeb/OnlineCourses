train_size, valid_size = 800, 200
# Define a sequence of indices from 0 to size of en_text
inds = np.arange(len(en_text))
np.random.shuffle(inds)
# Define train_inds as first train_size indices
train_inds = inds[:train_size]
valid_inds = inds[train_size:train_size+valid_size]
# Define tr_en (train EN sentences) and tr_fr (train FR sentences)
tr_en = [en_text[ti] for ti in train_inds]
tr_fr = [fr_text[ti] for ti in train_inds]
# Define v_en (valid EN sentences) and v_fr (valid FR sentences)
v_en = [en_text[vi] for vi in valid_inds]
v_fr = [fr_text[vi] for vi in valid_inds]
print('Training (EN):\n', tr_en[:3], '\nTraining (FR):\n', tr_fr[:3])
print('\nValid (EN):\n', v_en[:3], '\nValid (FR):\n', v_fr[:3])
