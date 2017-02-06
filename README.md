# cloudfront_invalidator

This simple python script will invalidate AWS cloudfront cache for a given distro ID. Intended for use with travis-ci, but should be easily adaptable to other circumstances.

## Setup

Requires boto:
`pip install boto`

Change the placeholders `<replace with cloudfront distro id>` in the file `invalidator.py` to reflect your distro ids. 


## Example usage in a travis.yml:

```
after_deploy:
- pip install --user boto
- python cloudfront_invalidation.py -a $AWS_ACCESS_KEY -s $AWS_SECRET_KEY -b $TRAVIS_BRANCH
```

In the above example, one is required to set the `AWS_ACCESS_KEY` and `AWS_SECRET_KEY` environment variables. `TRAVIS_BRANCH` is always available.
