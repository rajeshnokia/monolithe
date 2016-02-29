# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from copy import deepcopy


def apply_extension(extension, specification):

    if "model" in extension:
        if "model" not in specification:
            specification["model"] = {}

        for key, value in extension["model"].iteritems():
            if value is not None:
                if key not in specification["model"] or specification["model"][key] is None:
                    specification["model"][key] = value

    if "attributes" in extension:
        if "attributes" not in specification:
            specification["attributes"] = []

        for attr in extension["attributes"]:
            attribute_name = attr["name"]

            found = False
            for a in specification["attributes"]:
                if a["name"] == attribute_name:
                    found = True
                    break

            if not found:
                specification["attributes"].append(attr)

    if "children" in extension:
        if "children" not in specification:
            specification["children"] = []

        for api in extension["children"]:
            api_name = api["rest_name"]

            found = False
            for a in specification["children"]:
                if a["rest_name"] == api_name:
                    found = True
                    break

            if not found:
                specification["children"].append(api)
