 {
  "grid": {
    "layers": {
      "Default layer": {
        "name": "Default layer"
      },
      "Admin": {
        "name": "Admin"
      },
      "Form": {
        "name": "Form"
      },
      "StructureInfo": {
        "name": "StructureInfo"
      }
    },
    "xWidth": 10,
    "yHeight": 10
  },
  "version": "2.121.2",
  "modules": [
    {
      "url": "modules/types/science/chemistry/jsmol/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "script": [
                null
              ],
              "syncScript": [
                null
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 36,
            "top": 0
          },
          "size": {
            "width": 71,
            "height": 79
          },
          "zIndex": 0,
          "display": true,
          "title": "3D structure",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 7,
            "top": 2
          },
          "size": {
            "width": 45,
            "height": 42
          },
          "zIndex": 0,
          "display": true,
          "title": "3D structure",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Form": {
          "position": {
            "left": 49,
            "top": 0
          },
          "size": {
            "width": 45,
            "height": 42
          },
          "zIndex": 0,
          "display": false,
          "title": "3D structure",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "StructureInfo": {
          "position": {
            "left": 35,
            "top": 0
          },
          "size": {
            "width": 63,
            "height": 64
          },
          "zIndex": 0,
          "display": false,
          "title": "3D structure",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 1,
      "vars_in": [
        {
          "rel": "data",
          "name": "model"
        }
      ],
      "actions_in": [
        {
          "rel": "jsmolscript",
          "name": "command"
        }
      ],
      "title": "3D structure",
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "zindex": 2,
      "toolbar": {
        "custom": [
          [
            {
              "title": "Copy file",
              "icon": "fa-copy",
              "action": "Copy",
              "position": "begin"
            },
            {
              "title": "Show log",
              "icon": " fa-plus-circle",
              "action": "showLog",
              "position": "begin"
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Show fullscreen"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ]
    },
    {
      "url": "modules/types/client_interaction/dragdrop/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "label": [
                "Drop or paste a PDB, CIF or molfile 3d"
              ],
              "dragoverlabel": [
                null
              ],
              "hoverlabel": [
                "Drop or paste a PDB, CIF or molfile 3d"
              ],
              "fileSelectLabel": [
                "Select file"
              ],
              "labelFontSize": [
                22
              ],
              "checkOptions": [
                [
                  "promptAmbiguous"
                ]
              ],
              "inputOptions": [
                [
                  "allowDrop",
                  "allowPaste",
                  "allowFileInput"
                ]
              ]
            }
          ],
          "vars": [
            [
              {
                "filter": "ext",
                "extension": "*",
                "filetype": "text",
                "type": "",
                "variable": "file"
              }
            ]
          ],
          "string_general": [
            {
              "askFilename": [
                []
              ]
            }
          ],
          "string": [
            [
              {
                "filter": "ext",
                "extension": "*",
                "type": "",
                "variable": "file"
              }
            ]
          ],
          "photo": [
            [
              {
                "variable": "photo"
              }
            ]
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 19
          },
          "size": {
            "width": 35,
            "height": 11
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": false,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 54
          },
          "size": {
            "width": 34,
            "height": 9
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 54
          },
          "size": {
            "width": 34,
            "height": 9
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 19
          },
          "size": {
            "width": 34,
            "height": 7
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": false,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 2,
      "title": "",
      "vars_out": [
        {
          "event": "onRead",
          "rel": "data",
          "jpath": [
            "file",
            "content"
          ],
          "name": "model"
        }
      ],
      "vars_in": [],
      "actions_in": [
        {}
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              []
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "zindex": 1
    },
    {
      "url": "modules/types/client_interaction/code_editor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "mode": [
                "text"
              ],
              "outputType": [
                null
              ],
              "btnvalue": [
                "Show unit cell"
              ],
              "iseditable": [
                [
                  "editable"
                ]
              ],
              "hasButton": [
                [
                  "button"
                ]
              ],
              "variable": [
                []
              ],
              "storeOnChange": [
                [
                  "store"
                ]
              ],
              "debouncing": [
                0
              ],
              "script": [
                "unitcell on;\nunitcell BOUNDBOX;\nunitcell 0.1;\n\nset axesUnitCell;\naxes 0.2;\nshow symmetry\nset showUnitCell on"
              ]
            }
          ],
          "ace": [
            {
              "useSoftTabs": [
                [
                  "yes"
                ]
              ],
              "tabSize": [
                4
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 57
          },
          "size": {
            "width": 35,
            "height": 22
          },
          "zIndex": 0,
          "display": true,
          "title": "You may write here JMol code",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 63,
            "top": 45
          },
          "size": {
            "width": 44,
            "height": 25
          },
          "zIndex": 0,
          "display": false,
          "title": "You may write here JMol code",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Form": {
          "position": {
            "left": 63,
            "top": 45
          },
          "size": {
            "width": 44,
            "height": 25
          },
          "zIndex": 0,
          "display": false,
          "title": "You may write here JMol code",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "StructureInfo": {
          "position": {
            "left": 99,
            "top": 4
          },
          "size": {
            "width": 35,
            "height": 17
          },
          "zIndex": 0,
          "display": false,
          "title": "You may write here JMol code",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 3,
      "vars_in": [
        {}
      ],
      "actions_in": [
        {
          "rel": "_editPreferences",
          "name": "command"
        }
      ],
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "title": "You may write here JMol code",
      "actions_out": [
        {
          "event": "onButtonClick",
          "rel": "data",
          "jpath": [],
          "name": "command"
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              []
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "zindex": 1
    },
    {
      "url": "modules/types/display/template-twig/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "selectable": [
                []
              ],
              "template": [
                ""
              ],
              "modifyInForm": [
                []
              ],
              "debouncing": [
                250
              ],
              "formOptions": [
                [
                  "keepFormValueIfDataUndefined"
                ]
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 31
          },
          "size": {
            "width": 35,
            "height": 21
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 48,
            "height": 30
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Form": {
          "position": {
            "left": 1,
            "top": 0
          },
          "size": {
            "width": 48,
            "height": 46
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 31
          },
          "size": {
            "width": 34,
            "height": 33
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 4,
      "vars_in": [
        {
          "rel": "tpl",
          "name": "twigTemplate"
        }
      ],
      "actions_in": [
        {}
      ],
      "title": "",
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "vars_out": [
        {
          "event": "onFormChanged",
          "rel": "form",
          "jpath": [],
          "name": "form"
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              []
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "zindex": 1
    },
    {
      "url": "modules/types/client_interaction/code_editor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "mode": [
                "html"
              ],
              "outputType": [
                null
              ],
              "btnvalue": [
                "Send script"
              ],
              "iseditable": [
                [
                  "editable"
                ]
              ],
              "hasButton": [
                []
              ],
              "variable": [
                []
              ],
              "storeOnChange": [
                [
                  "store"
                ]
              ],
              "debouncing": [
                100
              ],
              "script": [
                "<style>\n    #jsMolPrefs th {\n        text-align: left;\n    )\n</style>\n\n<div id='jsMolPrefs'>\n<h2>3D Model preferences</h2>\n<table>\n    <tr>\n        <th>Atom size</th>\n        <td><input type=\"range\" name=\"cpk\" step=1 min=0 max=100 value=20></td>\n    </tr>\n    <tr>\n        <th>Bond size</th>\n        <td><input type=\"range\" name=\"wireframe\" step=0.01 min=0 max=0.99></td>\n    </tr>\n    <tr>\n        <th>Atom color</th>\n        <td>\n            <input type=\"color\" name=\"atomColor\">\n            Default:<input type='checkbox' name='atomColorDefault' checked>\n        </td>\n    </tr>\n    <tr>\n        <th>Bond color</th>\n        <td>\n            <input type=\"color\" name=\"bondColor\">\n            Default:<input type='checkbox' name='bondColorDefault' checked>\n        </td>\n    </tr>\n</table>\n<h2>Options</h2>\n<table>\n    <tr>\n        <td>\n            <input type='checkbox' name='isosurfaceDisplay' checked>\n        </td>\n        <th>Isosurface</th>\n        <td>\n            <input type=\"color\" name=\"isosurfaceColor\" value=\"#00ff00\">\n            Solvent size: <input type='text' name=\"isosurfaceSA\" value=\"1.4\" size=4>\n            Translucent: <input type='text' name=\"isosurfaceTranslucent\" value=\"0.9\" size=4>\n        </td>\n    </tr>\n</table>\n</div>\n\n"
              ]
            }
          ],
          "ace": [
            {
              "useSoftTabs": [
                [
                  "yes"
                ]
              ],
              "tabSize": [
                4
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 31
          },
          "size": {
            "width": 48,
            "height": 45
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 51,
            "top": 0
          },
          "size": {
            "width": 76,
            "height": 71
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 5,
      "vars_in": [
        {}
      ],
      "actions_in": [
        {}
      ],
      "vars_out": [
        {
          "event": "onEditorChange",
          "rel": "data",
          "jpath": [],
          "name": "twigTemplate"
        }
      ],
      "title": "",
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "zindex": 1
    },
    {
      "url": "modules/types/client_interaction/code_executor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "display": [
                [
                  "editor",
                  "buttons"
                ]
              ],
              "execOnLoad": [
                []
              ],
              "script": [
                "var form=get('form');\nvar previous=API.cache('previous');\n\nvar diff=getDiff(form, previous);\n\nconsole.log(diff)\nvar command=[];\n\nfor (var key of Object.keys(diff)) {\n    var value=diff[key];\n    switch (key) {\n        case 'cpk':\n            command.push('cpk '+value+'%');\n            break;\n        case 'wireframe':\n            command.push('wireframe '+value);\n            break; \n        case 'atomColorDefault':\n            if (value===true) {\n                command.push('color atoms cpk');\n                break;\n            }\n        case 'atomColor':\n            command.push('color atoms \"'+form.atomColor+'\"');\n            break;\n        case 'bondColorDefault':\n            if (value===true) {\n                command.push('color bonds cpk');\n                break;\n            }\n        case 'bondColor':\n            command.push('color bonds \"'+form.bondColor+'\"');\n            break;\n        case \"isosurfaceDisplay\":\n        case \"isosurfaceColor\":\n        case \"isosurfaceSize\":\n        case \"isosurfaceTranslucent\":\n            if (form.isosurfaceDisplay) {\n                command.push(\n                    'isosurface sasurface '+\n                    (form.isosurfaceSA || 1.4) +\n                    ' translucent ' + (form.isosurfaceTranslucent || 0.9) +\n                    ' \"'+form.isosurfaceColor+'\"');\n            } else {\n                command.push('isosurface off');\n            }\n            break;\n    }\n}\n\nAPI.doAction('command', command.join('\\r'));\n\nfunction getDiff(current = {}, previous = {}) {\n    var diff={};\n    for (var key of Object.keys(current)) {\n        if (current[key] !== previous[key]) {\n            diff[key]=current[key];\n        }\n    }\n    return diff;\n}\n\n\n\nAPI.cache('previous', form);"
              ],
              "asyncAwait": [
                []
              ]
            }
          ],
          "libs": [
            [
              {}
            ]
          ],
          "buttons": [
            [
              {
                "name": "button1",
                "label": "Execute",
                "hide": []
              }
            ]
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 53,
            "top": 2
          },
          "size": {
            "width": 75,
            "height": 32
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 95,
            "top": 0
          },
          "size": {
            "width": 75,
            "height": 42
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 6,
      "vars_in": [
        {
          "rel": "inputValue",
          "name": "form",
          "filter": ""
        }
      ],
      "actions_in": [
        {}
      ],
      "title": "",
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin"
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "zindex": 1
    },
    {
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "append": [
                []
              ],
              "maxEntries": [
                1
              ],
              "editable": [
                []
              ],
              "editSearchRegexp": [
                null
              ],
              "editReplace": [
                null
              ],
              "debounce": [
                0
              ],
              "defaultvalue": [
                "<h1><a href=\"http://chemapps.stolaf.edu/jmol/docs/\" target=\"_blank\">Scripting HELP</a></h1>\n"
              ],
              "font": [
                null
              ],
              "fontcolor": [
                [
                  0,
                  0,
                  0,
                  1
                ]
              ],
              "fontsize": [
                null
              ],
              "align": [
                null
              ],
              "valign": [
                null
              ],
              "rendererOptions": [
                ""
              ],
              "forceType": [
                ""
              ],
              "sprintf": [
                null
              ],
              "sprintfOrder": [
                null
              ],
              "preformatted": [
                []
              ]
            }
          ]
        }
      },
      "id": 7,
      "vars_in": [
        {}
      ],
      "actions_in": [
        {}
      ],
      "vars_out": [
        {}
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "url": "modules/types/display/single_value/",
      "zindex": 2,
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 53,
            "right": 0
          },
          "size": {
            "width": 35,
            "height": 5
          },
          "display": true,
          "title": " ",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": false,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "StructureInfo": {
          "position": {
            "left": 104,
            "top": 0,
            "right": 0
          },
          "size": {
            "width": 26,
            "height": 5
          },
          "display": false,
          "title": " ",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": false,
          "created": true,
          "name": "Default layer"
        }
      },
      "title": " ",
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ]
    },
    {
      "url": "modules/types/client_interaction/code_executor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "display": [
                [
                  "editor",
                  "buttons"
                ]
              ],
              "execOnLoad": [
                []
              ],
              "asyncAwait": [
                []
              ],
              "script": [
                "var experimentalFile=get('experimentalFile');\n\nvar model='';\n\nAPI.createData('cif','');\n\nif (experimentalFile.cif && experimentalFile.cif.dUrl) {\n    model={\n        type:'pdb',\n        url: experimentalFile.cif.dUrl\n    }\n    API.createData('cif',model);\n} else if (experimentalFile.pdb && experimentalFile.pdb.dUrl) {\n    model={\n        type:'pdb',\n        url: experimentalFile.pdb.dUrl\n    }\n}\n\nAPI.createData('model', model);\n\n\n\n"
              ]
            }
          ],
          "libs": [
            [
              {}
            ]
          ],
          "buttons": [
            [
              {
                "name": "button1",
                "label": "Execute",
                "hide": []
              }
            ]
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 142,
            "top": 0
          },
          "size": {
            "width": 51,
            "height": 34
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 47
          },
          "size": {
            "width": 59,
            "height": 39
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 49,
            "top": 43
          },
          "size": {
            "width": 80,
            "height": 52
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "StructureInfo": {
          "position": {
            "left": 142,
            "top": 0
          },
          "size": {
            "width": 51,
            "height": 34
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 8,
      "vars_in": [
        {
          "rel": "inputValue",
          "name": "experimentalFile"
        }
      ],
      "actions_in": [
        {}
      ],
      "title": "",
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin"
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "zindex": 1,
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ]
    },
    {
      "url": "modules/types/edition/slick_grid/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "slickCheck": [
                [
                  "enableCellNavigation",
                  "rowNumbering",
                  "forceFitColumns",
                  "highlightScroll",
                  "editable"
                ]
              ],
              "copyPaste": [
                []
              ],
              "copyPasteOptions": [
                [
                  "newRows"
                ]
              ],
              "autoColumns": [
                []
              ],
              "toolbar": [
                []
              ],
              "colorjpath": [
                []
              ],
              "slick.defaultColumnWidth": [
                null
              ],
              "slick.rowHeight": [
                null
              ],
              "slick.headerRowHeight": [
                30
              ],
              "slick.selectionModel": [
                "row"
              ],
              "idProperty": [
                ""
              ],
              "filterType": [
                "pref"
              ],
              "filterRow": [
                "// Documentation: https://github.com/NPellet/visualizer/blob/9220df906db163190d73bd0852d1ae63221ddbfc/src/modules/types/edition/slick_grid/view.js#L1264-L1300"
              ],
              "customJpaths": [
                "pdb.dUrl,cif.dUrl,file.dUrl"
              ]
            }
          ],
          "cols": [
            [
              {
                "name": "Filename",
                "jpath": [],
                "editor": "none",
                "forceType": "",
                "formatter": "typerenderer",
                "copyFormatter": "default",
                "visibility": "both",
                "rendererOptions": "twig:'  {% if reference %}{{reference}}  {% else %}  {{jcamp.filename|split(\"/\",3)[2]}}  {{text.filename|split(\"/\",3)[2]}}  {{cdf.filename|split(\"/\",3)[2]}}  {{xml.filename|split(\"/\",3)[2]}}  {{pdf.filename|split(\"/\",3)[2]}}  {{pdb.filename|split(\"/\",3)[2]}}  {{cif.filename|split(\"/\",3)[2]}}  {{file.filename|split(\"/\",3)[2]}}  {% endif %}  '  ",
                "editorOptions": "",
                "width": 94,
                "hideColumn": []
              },
              {
                "name": "pdb",
                "jpath": [
                  "pdb",
                  "dUrl"
                ],
                "editor": "none",
                "forceType": "downloadLink",
                "formatter": "typerenderer",
                "copyFormatter": "default",
                "visibility": "both",
                "rendererOptions": "",
                "editorOptions": "",
                "width": 72,
                "hideColumn": []
              },
              {
                "name": "cif",
                "jpath": [
                  "cif",
                  "dUrl"
                ],
                "editor": "none",
                "forceType": "downloadLink",
                "formatter": "typerenderer",
                "copyFormatter": "default",
                "visibility": "both",
                "rendererOptions": "",
                "editorOptions": "",
                "width": 82,
                "hideColumn": []
              },
              {
                "name": "file",
                "jpath": [
                  "file",
                  "dUrl"
                ],
                "editor": "none",
                "forceType": "downloadLink",
                "formatter": "typerenderer",
                "copyFormatter": "default",
                "visibility": "both",
                "rendererOptions": "",
                "editorOptions": "",
                "width": 82,
                "hideColumn": []
              }
            ]
          ],
          "actionCols": [
            [
              {
                "backgroundColor": [
                  255,
                  255,
                  255,
                  0
                ],
                "color": [
                  0,
                  0,
                  0,
                  1
                ],
                "position": "end",
                "clickMode": "text"
              }
            ]
          ],
          "groupings": [
            [
              {
                "getter": []
              }
            ]
          ],
          "actionOutButtons": [
            [
              {}
            ]
          ],
          "data": [
            {
              "saveInView": [
                []
              ],
              "varname": [
                ""
              ],
              "data": [
                "[]"
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 35,
            "height": 18
          },
          "zIndex": 0,
          "display": true,
          "title": "Xray",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Report": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "Xray",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Report"
        },
        "Admin": {
          "position": {
            "left": 79,
            "top": 39
          },
          "size": {
            "width": 75,
            "height": 20
          },
          "zIndex": 0,
          "display": true,
          "title": "MS",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "TwigDebug": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "Xray",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "TwigDebug"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "MS",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "StructureInfo": {
          "position": {
            "left": 126,
            "top": 2
          },
          "size": {
            "width": 34,
            "height": 18
          },
          "zIndex": 0,
          "display": true,
          "title": "Xray",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 9,
      "vars_in": [
        {
          "rel": "list",
          "name": "xray"
        }
      ],
      "actions_in": [
        {}
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "vars_out": [
        {
          "event": "onRowActive",
          "rel": "row",
          "jpath": [],
          "name": "experimentalFile"
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              []
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": "MS"
    },
    {
      "url": "modules/types/client_interaction/code_executor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "display": [
                [
                  "editor",
                  "buttons"
                ]
              ],
              "execOnLoad": [
                []
              ],
              "asyncAwait": [
                [
                  "top"
                ]
              ],
              "script": [
                "var result=CIF.parse(get('model'));\n\nvar info={\n    a: result._cell_length_a,\n    b: result._cell_length_b,\n    c: result._cell_length_c,\n    alpha: result._cell_angle_alpha,\n    beta: result._cell_angle_beta,\n    gamma: result._cell_angle_gamma,\n    hm: result['_space_group_name_H-M_alt'] || result['_symmetry_space_group_name_H-M'],\n    hall: result._space_group_name_Hall || result._symmetry_space_group_name_Hall,\n}\n\ntry{\n    const poremat = new Poreprober.PoreMat(get('model'));\n    const density = (poremat.density *  10 ** 24).toFixed(2);\n    const porosity = poremat.porosity.toFixed(2);\n    const voidVolume = poremat.voidVolume.toFixed(2);\n    info.density = density; \n    info.porosity = porosity; \n    info.voidVolume = voidVolume;\n}catch (err) {\n    console.log('computing pore properties failed')\n}\n\n\n\n\nAPI.createData('info',info);\n"
              ]
            }
          ],
          "libs": [
            [
              {
                "lib": "CIF",
                "alias": "CIF"
              },
              {
                "lib": "Poreprober",
                "alias": "Poreprober"
              }
            ]
          ],
          "buttons": [
            [
              {
                "name": "button1",
                "label": "Execute",
                "hide": [],
                "disable": []
              }
            ]
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 80,
            "top": 63
          },
          "size": {
            "width": 64,
            "height": 33
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 131,
            "top": 46
          },
          "size": {
            "width": 40,
            "height": 33
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 10,
      "vars_in": [
        {
          "rel": "inputValue",
          "name": "model"
        }
      ],
      "actions_in": [
        {}
      ],
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": ""
    },
    {
      "url": "modules/types/display/template-twig/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "selectable": [
                [
                  "yes"
                ]
              ],
              "template": [
                ""
              ],
              "modifyInForm": [
                []
              ],
              "debouncing": [
                0
              ],
              "formOptions": [
                [
                  "keepFormValueIfDataUndefined"
                ]
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 108,
            "top": 0
          },
          "size": {
            "width": 37,
            "height": 62
          },
          "zIndex": 0,
          "display": true,
          "title": "Structure information",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "Structure information",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "Structure information",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 1
          },
          "size": {
            "width": 35,
            "height": 60
          },
          "zIndex": 0,
          "display": true,
          "title": "Structure information",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        }
      },
      "id": 11,
      "vars_in": [
        {
          "rel": "value",
          "name": "info"
        },
        {
          "rel": "tpl",
          "name": "InfoTemplate"
        }
      ],
      "actions_in": [
        {}
      ],
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              []
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": "Structure information"
    },
    {
      "url": "modules/types/client_interaction/code_editor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "mode": [
                "html"
              ],
              "outputType": [
                null
              ],
              "btnvalue": [
                "Send script"
              ],
              "iseditable": [
                [
                  "editable"
                ]
              ],
              "hasButton": [
                [
                  "button"
                ]
              ],
              "variable": [
                []
              ],
              "storeOnChange": [
                [
                  "store"
                ]
              ],
              "debouncing": [
                0
              ],
              "script": [
                "<style>\n    #cifInfo body, #cifInfo tbody {\n        font-size: 1.5em;\n    }\n    #cifInfo th {\n        text-align: left;\n    }\n    #cifInfo th, #cifInfo td {\n        padding: 4px;\n    }\n    #cifInfo p {\n    padding: 4px;\n    font-size: 1.2em;\n    }\n</style>\n{% if info.a %}\n<div id='cifInfo'>\n<h1>Cell information</h1>\n<table>\n    <tr>\n        <th>a</th>\n        <td>{{info.a}} Â</td>\n    </tr>\n    <tr>\n        <th>b</th>\n        <td>{{info.b}} Â</td>\n    </tr>\n    <tr>\n        <th>c</th>\n        <td>{{info.c}} Â</td>\n    </tr>\n    <tr>\n        <th>α</th>\n        <td>{{info.alpha}}</td>\n    </tr>\n    <tr>\n        <th>b</th>\n        <td>{{info.beta}}</td>\n    </tr>\n    <tr>\n        <th>ɣ</th>\n        <td>{{info.gamma}}</td>\n    </tr>\n    <tr>\n        <th>Hermann–Mauguin</th>\n        <td>{{info.hm}}</td>\n    </tr>\n    <tr>\n        <th>Hall symmetry</th>\n        <td>{{info.hall}}</td>\n    </tr>\n</table>\n{% endif %}\n<br>\n\n{% if info.density %}\n<h1>Pore properties</h1>\n\n<p>\nCalculated using the <a href='https://chemrxiv.org/articles/Systematic_Analysis_of_Porosities_in_Metal-Organic_Frameworks/10060331'> overlapping spheres (OSA) approach</a>, using atomic radii \nfrom the universal force field (UFF)\n</p>\n\n<table> \n    <tr>\n        <th>\n            void porosity ɸ\n        </th>\n        <td> \n            {{ info.porosity }}\n        </td>\n    </tr>\n    <tr>\n        <th>\n            void volume \n        </th>\n        <td> \n            {{ info.voidVolume }} Â<sup>3</sup>\n        </td>\n    </tr>\n    <tr>\n    <th>\n            density\n        </th>\n        <td> \n            {{ info.density }} g cm<sup>-3</sup>\n        </td>\n    </tr>\n</table>\n{% endif %}\n\n{% if topology.rcsr_name %}\n<h1>Pore properties</h1>\n<table>\n    <tr>\n        <th>\n            RSCR code\n        </th>\n        <td>\n            <a href=topology.link> topology.rcsr_name </a>\n        </td>\n    </tr>\n</table>\n{% endif %}\n\n</div>\n"
              ]
            }
          ],
          "ace": [
            {
              "useSoftTabs": [
                [
                  "yes"
                ]
              ],
              "tabSize": [
                4
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Form"
        },
        "StructureInfo": {
          "position": {
            "left": 36,
            "top": 1
          },
          "size": {
            "width": 88,
            "height": 73
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "StructureInfo"
        }
      },
      "id": 12,
      "vars_in": [
        {}
      ],
      "actions_in": [
        {}
      ],
      "vars_out": [
        {
          "event": "onEditorChange",
          "rel": "data",
          "jpath": [],
          "name": "InfoTemplate"
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": ""
    },
    {
      "url": "modules/types/edition/object_editor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "editable": [
                "view"
              ],
              "expanded": [
                []
              ],
              "storeObject": [
                []
              ],
              "displayValue": [
                []
              ],
              "searchBox": [
                [
                  "search"
                ]
              ],
              "sendButton": [
                []
              ],
              "output": [
                "new"
              ],
              "storedObject": [
                "{}"
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Form"
        },
        "StructureInfo": {
          "position": {
            "left": 126,
            "top": 24
          },
          "size": {
            "width": 50,
            "height": 49
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "StructureInfo"
        }
      },
      "id": 13,
      "vars_in": [
        {
          "rel": "value",
          "name": "info"
        }
      ],
      "actions_in": [
        {}
      ],
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": ""
    },
    {
      "url": "modules/types/client_interaction/code_executor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "display": [
                [
                  "editor",
                  "buttons"
                ]
              ],
              "execOnLoad": [
                []
              ],
              "asyncAwait": [
                [
                  "top"
                ]
              ],
              "script": [
                "const cif = get('cif').resurrect();\n\nvar event = getEvent();\nconsole.log(event);\n\nif (event == 'action') {\n    UI.progress('calculating', 'Calculating Topology');\n    \n    const body=JSON.stringify({\n        filecontent: cif,\n        extension: 'cif',\n    })\n    \n    const response = await fetch(\"https://crystal.cheminfo.org/topology\", {\n      \"referrer\": \"https://crystal.cheminfo.org/docs\",\n      \"referrerPolicy\": \"no-referrer-when-downgrade\",\n      \"body\": body,\n      \"method\": \"POST\",\n    });\n    \n    const json = await response.json();\n    \n    console.log(json);\n    \n    if ('rcsr_name' in json) {\n        API.createData('topology', {rcsr_name: json.rcsr_name, link: json.link_to_rcsr});\n    }\n    UI.stopProgress('calculating');\n}"
              ]
            }
          ],
          "libs": [
            [
              {
                "lib": "src/util/ui",
                "alias": "UI"
              }
            ]
          ],
          "buttons": [
            [
              {
                "name": "button1",
                "label": "Execute",
                "hide": [],
                "disable": []
              }
            ]
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 1,
            "top": 89
          },
          "size": {
            "width": 78,
            "height": 55
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Form"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "StructureInfo"
        }
      },
      "id": 14,
      "vars_in": [
        {
          "rel": "inputValue",
          "name": "cif"
        }
      ],
      "actions_in": [
        {
          "rel": "execute",
          "name": "exec"
        }
      ],
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": ""
    },
    {
      "url": "modules/types/client_interaction/code_executor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "display": [
                [
                  "editor",
                  "buttons"
                ]
              ],
              "execOnLoad": [
                []
              ],
              "asyncAwait": [
                [
                  "top"
                ]
              ],
              "script": [
                "const cif = get('cif').resurrect();\n\n\nlet body={\n    filecontent: cif,\n    extension: 'cif',\n}\n\nbody=\"{\\\"filecontent\\\":\\\"string\\\",\\\"extension\\\":\\\"string\\\"}\";\n\nbody={\n    filecontent: cif,\n    extension: 'cif',\n};\n\nconsole.log(body)\n\n\nlet response = await fetch(\"https://crystal.cheminfo.org/topology\", {\n  \"body\": JSON.stringify(body),\n  \"method\": \"POST\",\n});\n\n\nlet result = await response.json();\n\nconsole.log(result);"
              ]
            }
          ],
          "libs": [
            [
              {}
            ]
          ],
          "buttons": [
            [
              {
                "name": "button1",
                "label": "Execute",
                "hide": [],
                "disable": []
              }
            ]
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Form"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "StructureInfo"
        }
      },
      "id": 15,
      "vars_in": [
        {
          "rel": "inputValue",
          "name": "cif"
        }
      ],
      "actions_in": [
        {}
      ],
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": ""
    },
    {
      "url": "modules/types/client_interaction/button_action/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "toggle": [
                "click"
              ],
              "label": [
                "Compute topology information "
              ],
              "onLabel": [
                "Toggle action off"
              ],
              "offLabel": [
                "Toggle action on"
              ],
              "title": [
                ""
              ],
              "css": [
                "font-size: 11px;\nbackground-color: #E6E6E6;\nborder: 1px solid rgba(0, 0, 0, 0.2);\nheight: 30px;\npadding: .5em 1em;\nfont-weight: bold;"
              ],
              "cssOn": [
                "font-size: 11px;\nbackground-color: #E6E6E6;\nborder: 1px solid rgba(0, 0, 0, 0.2);\nheight: 30px;\npadding: .5em 1em;\nfont-weight: bold;"
              ],
              "cssOff": [
                "font-size: 11px;\nbackground-color: #E6E6E6;\nborder: 1px solid rgba(0, 0, 0, 0.2);\nheight: 30px;\npadding: .5em 1em;\nfont-weight: bold;"
              ],
              "startState": [
                "off"
              ],
              "text": [
                null
              ],
              "askConfirm": [
                []
              ],
              "confirmText": [
                "Are you sure?"
              ],
              "okLabel": [
                "Ok"
              ],
              "cancelLabel": [
                "Cancel"
              ],
              "contentType": [
                "content"
              ],
              "content": [
                ""
              ],
              "maskOpacity": [
                0.6
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 108,
            "top": 64
          },
          "size": {
            "width": 37,
            "height": 6
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": false,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Form"
        },
        "StructureInfo": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "StructureInfo"
        }
      },
      "id": 16,
      "vars_in": [],
      "actions_in": [
        {
          "rel": "activate"
        }
      ],
      "vars_out": [],
      "actions_out": [
        {
          "event": "onClick",
          "rel": "actionText",
          "jpath": [],
          "name": "exec"
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": ""
    },
    {
      "url": "modules/types/edition/object_editor/",
      "configuration": {
        "sections": {},
        "groups": {
          "group": [
            {
              "editable": [
                "view"
              ],
              "expanded": [
                []
              ],
              "storeObject": [
                []
              ],
              "displayValue": [
                []
              ],
              "searchBox": [
                [
                  "search"
                ]
              ],
              "sendButton": [
                []
              ],
              "output": [
                "new"
              ],
              "storedObject": [
                "{}"
              ]
            }
          ]
        }
      },
      "layers": {
        "Default layer": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Default layer"
        },
        "Admin": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Admin"
        },
        "Form": {
          "position": {
            "left": 0,
            "top": 0
          },
          "size": {
            "width": 20,
            "height": 20
          },
          "zIndex": 0,
          "display": false,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "Form"
        },
        "StructureInfo": {
          "position": {
            "left": 98,
            "top": 79
          },
          "size": {
            "width": 51,
            "height": 25
          },
          "zIndex": 0,
          "display": true,
          "title": "",
          "bgColor": [
            255,
            255,
            255,
            0
          ],
          "wrapper": true,
          "created": true,
          "name": "StructureInfo"
        }
      },
      "id": 17,
      "vars_in": [
        {
          "rel": "value",
          "name": "topology"
        }
      ],
      "actions_in": [
        {}
      ],
      "vars_out": [
        {
          "jpath": []
        }
      ],
      "actions_out": [
        {
          "jpath": []
        }
      ],
      "toolbar": {
        "custom": [
          [
            {
              "title": "",
              "icon": "",
              "action": "",
              "position": "begin",
              "color": [
                100,
                100,
                100,
                1
              ]
            }
          ]
        ],
        "common": [
          {
            "toolbar": [
              [
                "Open Preferences"
              ]
            ]
          }
        ]
      },
      "css": [
        {
          "fontSize": [
            ""
          ],
          "fontFamily": [
            ""
          ]
        }
      ],
      "title": ""
    }
  ],
  "variables": [
    {
      "jpath": [
        ""
      ]
    }
  ],
  "configuration": {
    "title": "Generate or visualize a 3D model"
  },
  "actionscripts": [
    {
      "sections": {},
      "groups": {
        "action": [
          {
            "name": [
              "Copy"
            ],
            "script": [
              "require(['src/util/ui'], function(ui) {\n    var model = String(API.getData('model').get());\n    \n    if(!model) {\n        ui.showNotification('Please create a model first');   \n        return;\n    }\n    ui.showCode({\n        mode: 'text',\n        content: model,\n    });\n})    "
            ]
          }
        ]
      }
    },
    {
      "sections": {},
      "groups": {
        "action": [
          {
            "name": [
              "webserviceLoaded"
            ],
            "script": [
              "API.cache('webserviceLoaded', true);\n"
            ]
          }
        ]
      }
    },
    {
      "sections": {},
      "groups": {
        "action": [
          {
            "name": [
              "showLog"
            ],
            "script": [
              "require(['src/util/ui'], function(ui) {\n    var log = String(API.getData('log').get());\n    \n    if(!log) {\n        ui.showNotification('Please create a model first');   \n        return;\n    }\n    ui.showCode({\n        mode: 'text',\n        content: log,\n    });\n})    "
            ]
          }
        ]
      }
    }
  ],
  "init_script": [
    {
      "sections": {},
      "groups": {
        "general": [
          {
            "script": [
              "if (typeof IframeBridge !== 'undefined') {\n    IframeBridge.onMessage(onMessage);\n    IframeBridge.ready();\n    function onMessage(data) {\n        if (data.type === 'tab.data') {\n            if (data.message && data.message.uuid) {\n                require(['vh/eln/Sample'], function(Sample) {\n                    var sample = new Sample(data.message.couchDB, data.message.uuid, 'sample', {\n                        track:false\n                    });\n                });\n            }\n        }\n        if (data.type === 'tab.focus') {};\n    }\n}\n"
            ]
          }
        ]
      }
    }
  ],
  "actionfiles": [
    {
      "sections": {},
      "groups": {
        "action": [
          [
            {}
          ]
        ]
      }
    }
  ],
  "aliases": [
    {
      "path": "../../github/cheminfo-js/visualizer-helper/539a64cd19ee79239dee7a67fc09f3430618fedb/",
      "alias": "vh"
    },
    {
      "path": "../../lib/cif-parser/1.0.1/cif-parser.min",
      "alias": "CIF"
    },
    {
      "path": "../../lib/poreprober/HEAD/poreprober.min",
      "alias": "Poreprober"
    }
  ],
  "custom_filters": [
    {
      "sections": {
        "modules": [
          {
            "sections": {},
            "groups": {
              "modules": [
                [
                  {}
                ]
              ]
            }
          }
        ],
        "filtersLib": [
          {
            "sections": {},
            "groups": {
              "filters": [
                [
                  {}
                ]
              ]
            }
          }
        ],
        "filters": [
          {
            "sections": {},
            "groups": {
              "filter": [
                {
                  "name": [
                    null
                  ],
                  "script": [
                    null
                  ]
                }
              ],
              "libs": [
                [
                  {}
                ]
              ]
            }
          }
        ]
      },
      "groups": {}
    }
  ]
}