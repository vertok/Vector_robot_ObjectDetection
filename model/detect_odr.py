import os
import numpy as np
import cv2
import tensorflow as tf


class_list = ['Tortoise', 'Container', 'Magpie', 'Sea turtle', 'Football', 'Ambulance', 'Ladder', 'Toothbrush', 'Syringe',
 'Sink', 'Toy', 'Organ', 'Cassette deck', 'Apple', 'Human eye', 'Cosmetics', 'Paddle', 'Snowman', 'Beer', 'Chopsticks',
 'Human beard', 'Bird', 'Parking meter', 'Traffic light', 'Croissant', 'Cucumber', 'Radish', 'Towel', 'Doll', 'Skull',
 'Washing machine', 'Glove', 'Tick', 'Belt', 'Sunglasses', 'Banjo', 'Cart', 'Ball', 'Backpack', 'Bicycle', 'Home appliance',
 'Centipede', 'Boat', 'Surfboard', 'Boot', 'Headphones', 'Hot dog', 'Shorts', 'Fast food', 'Bus', 'Boy', 'Screwdriver',
 'Bicycle wheel', 'Barge', 'Laptop', 'Miniskirt', 'Drill', 'Dress', 'Bear', 'Waffle', 'Pancake', 'Brown bear', 'Woodpecker',
 'Blue jay', 'Pretzel', 'Bagel', 'Tower', 'Teapot', 'Person', 'Bow and arrow', 'Swimwear', 'Beehive', 'Brassiere', 'Bee',
 'Bat', 'Starfish', 'Popcorn', 'Burrito', 'Chainsaw', 'Balloon', 'Wrench', 'Tent', 'Vehicle registration plate', 'Lantern',
 'Toaster', 'Flashlight', 'Billboard', 'Tiara', 'Limousine', 'Necklace', 'Carnivore', 'Scissors', 'Stairs', 'Computer keyboard', 'Printer', 'Traffic sign', 'Chair', 'Shirt', 'Poster', 'Cheese', 'Sock', 'Fire hydrant', 'Land vehicle', 'Earrings',
 'Tie', 'Watercraft', 'Cabinetry', 'Suitcase', 'Muffin', 'Bidet', 'Snack', 'Snowmobile', 'Clock', 'Medical equipment',
 'Cattle', 'Cello', 'Jet ski', 'Camel', 'Coat', 'Suit', 'Desk', 'Cat', 'Bronze sculpture', 'Juice', 'Gondola', 'Beetle', 'Cannon',
 'Computer mouse', 'Cookie', 'Office building', 'Fountain', 'Coin', 'Calculator', 'Cocktail', 'Computer monitor', 'Box',
 'Stapler', 'Christmas tree', 'Cowboy hat', 'Hiking equipment', 'Studio couch', 'Drum', 'Dessert', 'Wine rack', 'Drink',
 'Zucchini', 'Ladle', 'Human mouth', 'Dairy', 'Dice', 'Oven', 'Dinosaur', 'Ratchet', 'Couch', 'Cricket ball', 'Winter melon', 'Spatula', 'Whiteboard', 'Pencil sharpener', 'Door', 'Hat', 'Shower', 'Eraser', 'Fedora', 'Guacamole',
 'Dagger', 'Scarf', 'Dolphin', 'Sombrero', 'Tin can', 'Mug', 'Tap', 'Harbor seal', 'Stretcher', 'Can opener', 'Goggles',
 'Human body', 'Roller skates', 'Coffee cup', 'Cutting board', 'Blender', 'Plumbing fixture', 'Stop sign', 'Office supplies', 'Volleyball', 'Vase', 'Slow cooker', 'Wardrobe', 'Coffee', 'Whisk', 'Paper towel', 'Personal care', 'Food',
 'Sun hat', 'Tree house', 'Flying disc', 'Skirt', 'Gas stove', 'Salt and pepper shakers', 'Mechanical fan', 'Face powder', 'Fax', 'Fruit', 'French fries', 'Nightstand', 'Barrel', 'Kite', 'Tart', 'Treadmill', 'Fox', 'Flag', 'Horn', 'Window blind', 'Human foot', 'Golf cart', 'Jacket', 'Egg', 'Street light', 'Guitar', 'Pillow', 'Human leg', 'Isopod', 'Grape', 'Human ear', 'Power plugs and sockets', 'Panda', 'Giraffe', 'Woman', 'Door handle', 'Rhinoceros', 'Bathtub', 'Goldfish',
 'Houseplant', 'Goat', 'Baseball bat', 'Baseball glove', 'Mixing bowl', 'Marine invertebrates', 'Kitchen utensil', 'Light switch', 'House', 'Horse', 'Stationary bicycle', 'Hammer', 'Ceiling fan', 'Sofa bed', 'Adhesive tape', 'Harp', 'Sandal',
 'Bicycle helmet', 'Saucer', 'Harpsichord', 'Human hair', 'Heater', 'Harmonica', 'Hamster', 'Curtain', 'Bed', 'Kettle',
 'Fireplace', 'Scale', 'Drinking straw', 'Insect', 'Hair dryer', 'Kitchenware', 'Indoor rower', 'Invertebrate', 'Food processor', 'Bookcase', 'Refrigerator', 'Wood-burning stove', 'Punching bag', 'Common fig', 'Cocktail shaker',
 'Jaguar', 'Golf ball', 'Fashion accessory', 'Alarm clock', 'Filing cabinet', 'Artichoke', 'Table', 'Tableware', 'Kangaroo',
 'Koala', 'Knife', 'Bottle', 'Bottle opener', 'Lynx', 'Lavender', 'Lighthouse', 'Dumbbell', 'Human head', 'Bowl',
 'Humidifier', 'Porch', 'Lizard', 'Billiard table', 'Mammal', 'Mouse', 'Motorcycle', 'Musical instrument', 'Swim cap',
 'Frying pan', 'Snowplow', 'Bathroom cabinet', 'Missile', 'Bust', 'Man', 'Waffle iron', 'Milk', 'Ring binder', 'Plate',
 'Mobile phone', 'Baked goods', 'Mushroom', 'Crutch', 'Pitcher', 'Mirror', 'Lifejacket', 'Table tennis racket', 'Pencil case', 'Musical keyboard', 'Scoreboard', 'Briefcase', 'Kitchen knife', 'Nail', 'Tennis ball', 'Plastic bag', 'Oboe', 'Chest of drawers', 'Ostrich', 'Piano', 'Girl', 'Plant', 'Potato', 'Hair spray', 'Sports equipment', 'Pasta', 'Penguin', 'Pumpkin',
 'Pear', 'Infant bed', 'Polar bear', 'Mixer', 'Cupboard', 'Jacuzzi', 'Pizza', 'Digital clock', 'Pig', 'Reptile', 'Rifle', 'Lipstick',
 'Skateboard', 'Raven', 'High heels', 'Red panda', 'Rose', 'Rabbit', 'Sculpture', 'Saxophone', 'Shotgun', 'Seafood',
 'Submarine sandwich', 'Snowboard', 'Sword', 'Picture frame', 'Sushi', 'Loveseat', 'Ski', 'Squirrel', 'Tripod',
 'Stethoscope', 'Submarine', 'Scorpion', 'Segway', 'Training bench', 'Snake', 'Coffee table', 'Skyscraper', 'Sheep',
 'Television', 'Trombone', 'Tea', 'Tank', 'Taco', 'Telephone', 'Torch', 'Tiger', 'Strawberry', 'Trumpet', 'Tree', 'Tomato',
 'Train', 'Tool', 'Picnic basket', 'Cooking spray', 'Trousers', 'Bowling equipment', 'Football helmet', 'Truck',
 'Measuring cup', 'Coffeemaker', 'Violin', 'Vehicle', 'Handbag', 'Paper cutter', 'Wine', 'Weapon', 'Wheel', 'Worm',
 'Wok', 'Whale', 'Zebra', 'Auto part', 'Jug', 'Pizza cutter', 'Cream', 'Monkey', 'Lion', 'Bread', 'Platter', 'Chicken',
 'Eagle', 'Helicopter', 'Owl', 'Duck', 'Turtle', 'Hippopotamus', 'Crocodile', 'Toilet', 'Toilet paper', 'Squid', 'Clothing',
 'Footwear', 'Lemon', 'Spider', 'Deer', 'Frog', 'Banana', 'Rocket', 'Wine glass', 'Countertop', 'Tablet computer','Waste container', 'Swimming pool', 'Dog', 'Book', 'Elephant', 'Shark', 'Candle', 'Leopard', 'Axe', 'Hand dryer', 'Soap dispenser', 'Porcupine', 'Flower', 'Canary', 'Cheetah', 'Palm tree', 'Hamburger', 'Maple', 'Building', 'Fish', 'Lobster',
 'Asparagus', 'Furniture', 'Hedgehog', 'Airplane', 'Spoon', 'Otter', 'Bull', 'Oyster', 'Horizontal bar', 'Convenience store', 'Bomb', 'Bench', 'Ice cream', 'Caterpillar', 'Butterfly', 'Parachute', 'Orange', 'Antelope', 'Beaker', 'Moths and butterflies', 'Window', 'Closet', 'Castle', 'Jellyfish', 'Goose', 'Mule', 'Swan', 'Peach', 'Coconut', 'Seat belt', 'Raccoon',
 'Chisel', 'Fork', 'Lamp', 'Camera', 'Squash', 'Racket', 'Human face', 'Human arm', 'Vegetable', 'Diaper', 'Unicycle',
 'Falcon', 'Chime', 'Snail', 'Shellfish', 'Cabbage', 'Carrot', 'Mango', 'Jeans', 'Flowerpot', 'Pineapple', 'Drawer', 'Stool',
 'Envelope', 'Cake', 'Dragonfly', 'Sunflower', 'Microwave oven', 'Honeycomb', 'Marine mammal', 'Sea lion',
 'Ladybug', 'Shelf', 'Watch', 'Candy', 'Salad', 'Parrot', 'Handgun', 'Sparrow', 'Van', 'Grinder', 'Spice rack', 'Light bulb',
 'Corded phone', 'Sports uniform', 'Tennis racket', 'Wall clock', 'Serving tray', 'Kitchen & dining room table', 'Dog bed', 'Cake stand', 'Cat furniture', 'Bathroom accessory', 'Facial tissue holder', 'Pressure cooker', 'Kitchen appliance', 'Tire', 'Ruler', 'Luggage and bags', 'Microphone', 'Broccoli', 'Umbrella', 'Pastry', 'Grapefruit', 'Band-aid',
 'Animal', 'Bell pepper', 'Turkey', 'Lily', 'Pomegranate', 'Doughnut', 'Glasses', 'Human nose', 'Pen', 'Ant', 'Car',
 'Aircraft', 'Human hand', 'Skunk', 'Teddy bear', 'Watermelon', 'Cantaloupe', 'Dishwasher', 'Flute', 'Balance beam',
 'Sandwich', 'Shrimp', 'Sewing machine', 'Binoculars', 'Rays and skates', 'Ipod', 'Accordion', 'Willow', 'Crab',
 'Crown', 'Seahorse', 'Perfume', 'Alpaca', 'Taxi', 'Canoe', 'Remote control', 'Wheelchair', 'Rugby ball', 'Armadillo',
 'Maracas', 'Helmet']
model_path = "./data"
frozen_pb_file = os.path.join(model_path, 'frozen_inference_graph.pb')
f = tf.gfile.FastGFile(frozen_pb_file, 'rb')
graph_def = tf.GraphDef()
graph_def.ParseFromString(f.read())
sess = tf.Session()
sess.graph.as_default()
tf.import_graph_def(graph_def, name='')


slim = tf.contrib.slim
image = tf.placeholder(tf.float32, shape=[1, 224, 224, 3])


def object_detection(img_file):

    """Detect object classes by loading Frozen graph."""
    score_threshold = 0.60
    img_cv2 = cv2.imread(img_file)

    # Crop the image if bounding box is provided


    img_height, img_width, _ = img_cv2.shape
    img_in = img_cv2[:, :, [2, 1, 0]]  # BGR2RGB

    list_of_class = []
    list_of_scores = []
    list_of_bboxes = []
    if True:
        outputs = sess.run([sess.graph.get_tensor_by_name('num_detections:0'),
                        sess.graph.get_tensor_by_name('detection_scores:0'),
                        sess.graph.get_tensor_by_name('detection_boxes:0'),
                        sess.graph.get_tensor_by_name('detection_classes:0'),
                        sess.graph.get_tensor_by_name("SecondStagePostprocessor/scale_logits:0"),], feed_dict={
                           'image_tensor:0': img_in.reshape(1,
                                                            img_in.shape[0],
                                                            img_in.shape[1],
                                                            3)})
        num_detections = int(outputs[0])
        # Visualize detected bounding boxes.
        for i in range(num_detections):
            class_id = int(outputs[3][0][i])
            score = float(outputs[1][0][i])
            bbox = [float(v) for v in outputs[2][0][i]]
            if score > score_threshold:
                x = bbox[1] * img_width
                y = bbox[0] * img_height
                right = bbox[3] * img_width
                bottom = bbox[2] * img_height
                bboxes = []
                # append bbox values  to a list:
                bboxes.append(int(x))
                bboxes.extend([int(y), int(right), int(bottom)])
                list_of_bboxes.append(bboxes)
                list_of_scores.append("{0:.2f}".format(score))
                list_of_class.append(class_list[class_id-1])
    return list_of_class



