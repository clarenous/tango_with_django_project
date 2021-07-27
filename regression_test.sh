#!/bin/bash

WORKDIR=.regression_test

if [ ! -d $WORKDIR  ]; then
  mkdir $WORKDIR
fi

CLONED=$WORKDIR/.cloned

if [ ! -f $CLONED ]; then
  git clone https://github.com/maxwelld90/tango_with_django_2_code.git $WORKDIR/tango_with_django_2_code && touch $CLONED
fi

TEST_VECTOR_DIR=$WORKDIR/tango_with_django_2_code/progress_tests
CODE_DIR=rango
START_CHAPTER=5
END_CHAPTER=5

for i in $(seq $START_CHAPTER $END_CHAPTER); do
  echo ""
  echo "Perform regression testing for chapter $i"
  cp $TEST_VECTOR_DIR/tests_chapter$i.py $CODE_DIR/
  python manage.py test rango.tests_chapter$i
  rm $CODE_DIR/tests_chapter$i.py
  echo ""
done
