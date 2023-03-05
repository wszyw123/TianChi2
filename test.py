import oss2

for obj in oss2.ObjectIteratorV2(bucket,prefix='train_videos_part1/'):
    print(obj.key)
