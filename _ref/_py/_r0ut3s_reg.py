import random
import requests
import csv
from flask import render_template, url_for, flash, redirect,  Blueprint, jsonify, redirect
from app import db, bcrypt
from app.models import Baseprice, Spawn, Purchased, Player

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/test")
def test():
    pass
    return render_template('test.html')

@main.route("/display")     
def display():
    pass
    return render_template('display.html')
-
@main.route('/base/<int:round_no>')
def base_price(round_no):
    pass  # base prices are from Zillow House Value:City
    price_column = 'Round'+str(round_no)  # Round1,Round2

    base_prices = Baseprice.query.all()
    res = [
        {getattr(bp, 'BasePriceLabel'):
            getattr(bp, price_column),
         }
        for bp in base_prices

    ]
    flat = {}

    for d in res:
        pass
        for k, v in d.items():
            pass
            flat[k] = v

    return jsonify(flat)
    # return jsonify(res)


@main.route('/desc')
def zillow_desc():
    pass  # API route for item desc
    # full name of the column
    base_prices = Baseprice.query.all()
    res = {
        bpL.BasePriceLabel:
        {
            'BasePriceLabel': bp.BasePriceLabel,
            'RegionName': bp.RegionName,
            'StateName': bp.StateName,
            'State': bp.State,
            'Metro': bp.Metro,
            'CountyName': bp.CountyName,
            'BedrmCt': bp.BedrmCt,
            'RegionID': bp.RegionID,
            'SizeRank': bp.SizeRank,
        } for (bpL, bp) in zip(base_prices, base_prices)
    }
    return jsonify(res)

@main.route('/spawn/<int:spawnCount>/<int:roundNo>')
def spawn_api(spawnCount, roundNo):
    pass
    web = 'http://regropoly.herokuapp.com'
    url_desc = web+'/desc'  # api route for desc
    # fetch all descriptions
    api_descriptions = requests.get(url_desc).json()
    # fetch all labels
    api_labels = [k[0] for k in api_descriptions.items()]
    # fetch base prices for the round
    api_baseprices = requests.get(web + '/base/'+str(roundNo)).json()
    _rc = random.choice
    labels = [slot + _rc(api_labels) for slot in ['']*spawnCount]

    descs = [api_descriptions[bp_label] for bp_label in labels]

    round_bps = [api_baseprices[bp_label] for bp_label in labels]
    
    # these are the last three year's prices
    try: # make it work for round 01 02 03
        pass
        api_bp_01 = requests.get(web + '/base/'+str(roundNo-1)).json()
        bp_01 = [api_bp_01[bp_label] for bp_label in labels]
        try:
            pass
            api_bp_02 = requests.get(web + '/base/'+str(roundNo-2)).json()
            bp_02 = [api_bp_02[bp_label] for bp_label in labels]
            try:
                pass
                api_bp_03 = requests.get(web + '/base/'+str(roundNo-3)).json()    
                bp_03 = [api_bp_03[bp_label] for bp_label in labels]
            except:
                pass
                bp_03 = bp_02
        except:
            pass
            bp_02= bp_01
            bp_03= bp_01
    except:
        pass
        bp_01 = round_bps
        bp_02 = round_bps
        bp_03 = round_bps
    

    bedroom_counts = [  # required to generate random img url
        dsc.get('BedrmCt', 3)
        for dsc in descs
    ]
    img_ct = {  # jpeg files per bedroom count
        '1': 10, '2': 10, '3': 10, '4': 10, '5': 10,
    }
    img_urls = [  # random by br-count
        {'img_url': 'https://raw.githubusercontent.com/attila5287/regropoly-img/master/photos/'
         + str(br)
         + '/'
         + str(random.randint(0, img_ct[str(br)]-1))
         + '.jpeg'}
        for br in bedroom_counts
    ]

    diff_factor = 0.95 # adjust with difficulty level of game
    _rv = random.normalvariate #localize a global var
    objects = [
        {
            **desc, 
            **imgURL, 
            'base_price': bp, 
            'base_price01': bp1, 
            'base_price02': bp2, 
            'base_price03': bp3, 
            'purchase_price': round(_rv(bp, bp*.1) * diff_factor), 
            'purchase_round': roundNo
        } for (desc, imgURL, bp, roundNo, bp1, bp2, bp3 ) in zip(descs, img_urls, round_bps, [roundNo]*spawnCount, bp_01, bp_02, bp_03)
    ]
    
    houses = [
        Spawn(**obj) for obj in objects
    ]
    

    db.session.query(Spawn).delete()
    db.session.add_all(houses)
    db.session.commit()

    q_all = Spawn.query.all()  # query for all in db

    d = [{c.name: getattr(q, c.name)
          for c in q.__table__.columns} for q in q_all]

    return jsonify(d)


@main.route('/purchase/<int:spawnIndex>')
def purchase(spawnIndex):
    pass
    target = Spawn.query.get_or_404(spawnIndex)
    # cast into dictionaries 
    d = {c.name: getattr(target, c.name) for c in target.__table__.columns}
    _rv = random.normalvariate
    # # then add a few more k,v pairs then db
    d['forsale_price'] = round(_rv(d['base_price'], 10000))
    
    d['forsale_round'] = d['purchase_round']
    
    d.pop('id') # drop the spawned item id 
    db.session.add(Purchased(**d))
    db.session.commit()
    return jsonify(d)

@main.route('/purchased/<int:roundNo>')
def purchased_api(roundNo):
    pass
    q_all = [p for p in Purchased.query.all()]
    labels = [
        p.BasePriceLabel for p in q_all
    ]
    web = 'http://regropoly.herokuapp.com'
    url_base = web+'/base/'+ str(roundNo)  # fetch new prices
    api_baseprices = requests.get(web + '/base/'+str(roundNo)).json()
    round_bps = [api_baseprices[bp_label] for bp_label in labels]
    
    
    try: # make it work for round 01 02 03 where no prev's three rounds avlb
        pass
        api_bp_01 = requests.get(web + '/base/'+str(roundNo-1)).json()
        bp_01 = [api_bp_01[bp_label] for bp_label in labels]
        try:
            pass
            api_bp_02 = requests.get(web + '/base/'+str(roundNo-2)).json()
            bp_02 = [api_bp_02[bp_label] for bp_label in labels]
            try:
                pass
                api_bp_03 = requests.get(web + '/base/'+str(roundNo-3)).json()    
                bp_03 = [api_bp_03[bp_label] for bp_label in labels]
            except: # req'd for the first three rounds
                pass
                bp_03 = bp_02
        except: # req'd for the first three rounds
            pass
            bp_02= bp_01
            bp_03= bp_01
    except: # req'd for the first three rounds
        pass
        bp_01 = round_bps
        bp_02 = round_bps
        bp_03 = round_bps
    
    
    diff_factor = 1.05 # adjust with game difficulty level
    _rv = random.normalvariate # localize global variable
    
    for (p, bp, bp1, bp2, bp3) in zip(q_all, round_bps, bp_01, bp_02, bp_03):
        pass
        p.base_price = bp
        p.forsale_round = roundNo
        mean = p.base_price * diff_factor
        std = mean * .05
        p.forsale_price = round(_rv(mean, std))
        
        p.base_price01 = bp1 # price history
        p.base_price02 = bp2
        p.base_price03 = bp3

    d = [  # cast into dictionaries
         {
            c.name: getattr(q, c.name)
            for c in q.__table__.columns
        }
        for q in q_all
    ]
    
    db.session.commit() #save updated prices on objects     
    
    return jsonify(d)

@main.route('/sell/<int:id>/<int:s_price>')
def sell(id, s_price):
    pass
    q_sold = [Purchased.query.get_or_404(id)]
    
    d = [{c.name: getattr(q, c.name)
          for c in q.__table__.columns} for q in q_sold]
    
    return jsonify({
        'purchased_id': id,
        'forsale_price': q_sold[0].forsale_price,
        'base_price': q_sold[0].base_price,
        'data' : d[0]
    })


@main.route('/show/player/<int:id>')
def show_player(id):
    pass
    player_exists = Player.query.get(id)
    if player_exists:
        pass
        # query for db model Player
        q_display = [ Player.query.get(id) ]
        # cast into dictionary
        d = [{c.name: getattr(q, c.name)
            for c in q.__table__.columns} for q in q_display]
        return jsonify(  d[0]  )
    else:
      pass
      return jsonify( { 'player id {}'.format(id) : 'does not exist on Player database'}  )
      
      
@main.route('/add/player/<string:new_player_name>')
def add_player(new_player_name):
    pass
    existing_names = [
        p.player_name for p in Player.query.filter(Player.player_name == new_player_name)
    ]
    if new_player_name in existing_names:
        pass
        return jsonify({'player name':'already exists on Player database'})
        
    else:
        pass
        db.session.add(Player(
            avatar_url = 'https://raw.githubusercontent.com/attila5287/regropoly/master/app/static/profile_pics/attila.jpg', 
            player_name = new_player_name, 
            avlb_funds = 10000000, 
            high_worth = 10000000,  
            low_worth = 10000000,  
            rtn_on_inv = 0, 
            num_of_inv = 0 
        ))
        q_added = Player.query.filter(Player.player_name == new_player_name)
        
        d = [{c.name: getattr(q, c.name)
            for c in q.__table__.columns} for q in q_added]
        
        db.session.commit()
        return jsonify(  d[0]  )
