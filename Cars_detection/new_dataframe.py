"""
In this file we create a new dataframe that will match to yolo requiremets
"""

HEIGHT = 380
WIDTH = 676

def bounding_box(xmin,ymin,xmax,ymax):
    center = ((xmin+xmax)/2, (ymin+ymax)/2)
    x_center = center[0] / WIDTH
    y_center = center[1] / HEIGHT
    height = (ymax - ymin)/HEIGHT
    width = (xmax - xmin)/WIDTH
    return x_center, y_center, height, width

# create new dataframe with columns names - iamge,class, x_center, y_center, height, width
new_df = defaultdict(list)
for ind in df.index:
    xmin = df['xmin'][ind]
    xmax = df['xmax'][ind]
    ymin = df['ymin'][ind]
    ymax = df['ymax'][ind]
    x_cen,y_cen, h,w = bounding_box(xmin,ymin,xmax,ymax)
    new_df['image'].append(str(df['image'][ind]))
    new_df['class'].append('0')
    new_df['x_center'].append(x_cen)
    new_df['y_center'].append(y_cen)
    new_df['height'].append(h)
    new_df['width'].append(w)
    
    new_df = pd.DataFrame(new_df)
    new_df.head()