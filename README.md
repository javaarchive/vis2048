# vis2048

![Travis CI badge](https://travis-ci.org/Fylipp/vis2048.svg?branch=master)

An implementation of [2048](http://2048game.com) with visualization support and extensive tests.

![Screenshot of a demo with 4 simultaneous games](https://github.com/Fylipp/vis2048/blob/master/screenshot.png?raw=true)

## Installation

Via `pip`:

```
pip install vis2048
```

Or `git clone`:

```
git clone https://github.com/Fylipp/vis2048
cd vis2048
./setup.py install
```

## Testing

```
python -m unittest tests/test.py
```

## License
MIT.

# Docs

## vis2048.game.Game(width, min_tile, max_tile)
width is also height. Most likely you want `Game(4,2,2048)`
### won() -> boolean
Returns a boolean based on if you have reached max_tile.
### stuck() -> boolean
Returns a boolean based on if you can no longer move so basically if you have lost or not. 
### full() -> boolean
Is the board full?
### place_two()
Places a two randomly in a empty lace. 
### left,right,up,down
Executes the following move
