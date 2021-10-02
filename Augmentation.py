def build_ins_seg_train_aug(cfg):
    augs = [
        T.ResizeShortestEdge(ShortestEdge, max_size=MaxEdge), #(h, w)
        T.RandomFlip(prob=0.5, horizontal=False, vertical=True),
        T.RandomFlip(prob=0.5, horizontal=True, vertical=False),
        T.RandomApply(T.RandomBrightness(1-config['augIntensity'],1+config['augIntensity']), prob=0.5),
        T.RandomApply(T.RandomContrast(1-config['augIntensity'],1+config['augIntensity']), prob=0.5),
        T.RandomApply(T.RandomLighting(config['augIntensity']), prob=0.5),
        T.RandomApply(T.RandomRotation(range(0,360),expand=True), prob=0.5),
        T.RandomApply(T.RandomCrop_CategoryAreaConstraint("relative",(0.8,0.8), ignored_category=2), prob=0.2),
    ]

    return augs