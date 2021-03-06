"""@brief     Contains constants common to all modules of TTT."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################
#
# PyKeylogger: TTT for Linux and Windows
# Copyright (C) 2016 Roxana Lafuente <roxana.lafuente@gmail.com>
#                    Miguel Lemos <miguelemosreverte@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import os

def is_valid_dir(directory):
    """
    @brief     Determines if a directory is valid.

    @returnReturns True if directory is valid, False otherwise.
    """
    is_valid = directory is not None and directory != ""
    is_valid = is_valid and os.path.exists(directory)
    is_valid = is_valid and os.path.isdir(directory)
    return is_valid

def is_valid_file(filepath):
    """
    @brief     Determines if a file is valid.

    @returnReturns True if directory is valid, False otherwise.
    """
    is_valid = filepath is not None and filepath != ""
    is_valid = is_valid and os.path.exists(filepath)
    is_valid = is_valid and os.path.isfile(filepath)
    return is_valid

# Languages we show in the GUI to work with Moses.
languages = ["en", "es", "fr", "it", "ru", "cz", "ar", "pt", "de"]

# Config file where info from Moses is saved.
moses_dir_fn = "moses.config"

# Filenames.
train_fn = "training.out"

# Check OS
is_win = os.name == 'nt'

# Moses commands
tokenizer = "%s/scripts/tokenizer/tokenizer.perl "

truecaser_train = "%s/scripts/recaser/train-truecaser.perl "
model = "%s/truecase-model.%s"

truecaser = "%s/scripts/recaser/truecase.perl "

cleaner = "%s/scripts/training/clean-corpus-n.perl "

lm_train = "%s/bin/lmplz " + "--discount_fallback -o 3 "  # TODO: Should be chosen by the user.

blm_train = "%s/bin/build_binary "

tm_train = "nohup nice " + "%s/scripts/training/train-model.perl" + " -root-dir train "

test = "%s/bin/moses" + " -f "
