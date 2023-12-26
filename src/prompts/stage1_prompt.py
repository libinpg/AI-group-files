# prompts.py {}对应的参数依次为os.listdir(directory)的结果
CONCLUDE_DIRECTORY_PROMPT = (
    "To guess the file category and classify by files names to some keypoints in ```, your answer can not contain any info of my words' , only reply as [keypoint1,keypoint2,keypoint3...],keypoint should be meaningful "
    "you don't need to focus on specific file"
    "you should return a array,the length of array should be appropriate "
    "```'{}'```.  "
)