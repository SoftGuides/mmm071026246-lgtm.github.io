from pathlib import Path
import json

pages = [
    {
        'filename': 'dog-rash-itching-causes-explained.html',
        'title': 'Dog Rash and Itching Causes Explained',
        'description': 'Explore the common causes of dog rash and itching, how to identify the source, and steps to help your pet feel better.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-rash-itching-causes-explained.jpg',
        'sections': [
            ('Why dog rashes and itching appear', 'Rashes and itching can come from many sources, from allergies and parasites to infections and environmental irritants.', [
                'Contact with irritating plants or chemicals',
                'Flea bites or other insect bites',
                'Food sensitivities and allergies',
                'Dry air or seasonal changes',
                'Underlying skin infections',
                'Stress-related self-trauma'
            ]),
            ('Allergic triggers and skin reactions', 'Allergy-related skin symptoms are some of the most common reasons dogs scratch and develop rashes.', [
                'Atopic dermatitis from pollen, dust, or mold',
                'Food allergy causing red, itchy patches',
                'Contact allergy to shampoos, fabrics, or grass',
                'Medication reactions that involve the skin',
                'Flea saliva allergy leading to intense scratching',
                'Environmental irritants like smoke or perfume'
            ]),
            ('Infections that cause rash and itch', 'Bacterial, fungal, and parasitic infections can trigger visible skin changes and deep discomfort.', [
                'Yeast overgrowth in skin folds or ears',
                'Bacterial hotspots from secondary infection',
                'Ringworm causing circular, scaly patches',
                'Mange mites leading to widespread itching',
                'Fleas, ticks, and external parasites',
                'Ear infections that spread to surrounding skin'
            ]),
            ('How to tell if the rash is serious', 'Some rashes are temporary and mild, while others require veterinary evaluation and treatment.', [
                'Open sores or bleeding skin',
                'Rapid spread of redness or swelling',
                'Persistent scratching that damages the skin',
                'Fever or lethargy along with skin signs',
                'Unpleasant odor from the coat or skin',
                'Changes in behavior or appetite'
            ])
        ]
    },
    {
        'filename': 'dog-hair-loss-skin-irritation-warning-signs.html',
        'title': 'Dog Hair Loss and Skin Irritation Warning Signs',
        'description': 'Learn the warning signs of dog hair loss and skin irritation so you can act quickly when your pet needs care.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-hair-loss-skin-irritation-warning-signs.jpg',
        'sections': [
            ('Recognizing hair loss patterns', 'Hair loss in dogs can be localized or widespread, and the pattern helps indicate the underlying cause.', [
                'Circular bald patches with defined edges',
                'Thinning fur across the back or belly',
                'Clumps of hair left after scratching',
                'Smooth, shiny areas where the coat is gone',
                'Hair loss around the ears, paws, or tail',
                'Uneven coat density or patchiness'
            ]),
            ('Skin irritation signs to watch', 'Irritated skin often feels hot, looks red, and leads to chewing, licking, or rubbing.', [
                'Red or inflamed patches of skin',
                'Rash, bumps, or pimples',
                'Dry, flaky, or scaly texture',
                'Swollen or thickened skin',
                'Pain or sensitivity when touched',
                'Discoloration from repeated licking'
            ]),
            ('Common causes of hair loss and irritation', 'Multiple causes can lead to these symptoms, and identifying the cause is the first step to treatment.', [
                'Allergy-driven scratching and chewing',
                'Parasite infestations like fleas or mites',
                'Hormonal imbalance or thyroid issues',
                'Nutrition-related coat problems',
                'Physical trauma or self-inflicted wounds',
                'Dry skin from seasonal changes'
            ]),
            ('When hair loss needs veterinary help', 'Hair loss accompanied by irritation can progress quickly and should not be ignored.', [
                'Rapid spreading of the affected area',
                'Bleeding, open sores, or crusts',
                'Signs of infection like pus or smell',
                'Behavioral changes from discomfort',
                'Failure to improve with simple home care',
                'High fever or systemic illness'
            ])
        ]
    },
    {
        'filename': 'dog-contact-dermatitis-symptoms-prevention.html',
        'title': 'Dog Contact Dermatitis Symptoms and Prevention',
        'description': 'Understand dog contact dermatitis symptoms, common triggers, and how to prevent skin flare-ups at home.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-contact-dermatitis-symptoms-prevention.jpg',
        'sections': [
            ('What is contact dermatitis?', 'Contact dermatitis occurs when a dog’s skin reacts to a substance it touches, causing inflammation and discomfort.', [
                'Reaction to lawn chemicals or fertilizers',
                'Irritation from cleaning products or soaps',
                'Sensitivity to certain fabrics or bedding',
                'Reaction to grooming products or sprays',
                'Plant-based irritants like poison ivy or ivy',
                'Exposure to insect repellents or pesticides'
            ]),
            ('Symptoms of contact dermatitis', 'The condition often shows as red, itchy, or raw skin in areas that touched the trigger.', [
                'Localized redness and small bumps',
                'Intense licking or chewing at affected areas',
                'Dry, crusty, or scaly patches',
                'Hair loss over irritated regions',
                'Raw or painful-looking skin',
                'Blister-like lesions or scabs'
            ]),
            ('How to identify the trigger', 'Finding the cause can involve carefully reviewing exposure and the timing of symptoms.', [
                'Note recent changes in cleaning supplies',
                'Check new bedding, collars, or clothing',
                'Remember if your dog walked through new plants',
                'Look for patterns after grooming or bathing',
                'Consider topical medications recently applied',
                'Review any new products used around the dog'
            ]),
            ('Steps to prevent future episodes', 'Prevention focuses on reducing contact with known irritants and protecting the skin.', [
                'Rinse paws and legs after walks',
                'Use gentle, hypoallergenic grooming products',
                'Choose breathable bedding fabrics',
                'Avoid harsh lawn and household chemicals',
                'Create a safe indoor space during yard care',
                'Introduce new products slowly and monitor reactions'
            ])
        ]
    },
    {
        'filename': 'dog-food-allergy-skin-symptoms-checklist.html',
        'title': 'Dog Food Allergy Skin Symptoms Checklist',
        'description': 'Use this dog food allergy skin symptoms checklist to spot early signs of food-related reactions and know when to talk to a vet.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-food-allergy-skin-symptoms-checklist.jpg',
        'sections': [
            ('How food allergy affects the skin', 'Food allergies in dogs often show through skin-related symptoms rather than digestive upset.', [
                'Itchy skin that flares after meals',
                'Red, inflamed patches on the trunk or limbs',
                'Recurring ear infections or inflammation',
                'Hot spots and self-trauma from scratching',
                'Hair loss over irritated areas',
                'Swollen paws or face'
            ]),
            ('Common food allergy triggers', 'Certain protein and ingredient sources are more likely to cause allergic reactions in dogs.', [
                'Beef and dairy proteins',
                'Chicken or poultry exposures',
                'Grains like wheat, corn, and soy',
                'Artificial colors, flavors, or preservatives',
                'Novel proteins in treats or supplements',
                'Cross-reactivity with multiple protein sources'
            ]),
            ('Checklist for tracking skin symptoms', 'A systematic checklist helps you identify whether food could be the cause.', [
                'Does itching worsen after eating?',
                'Are skin signs seasonal or year-round?',
                'Do symptoms improve with a simple diet change?',
                'Are other causes like fleas or environment ruled out?',
                'Is there a history of similar symptoms in the past?',
                'Does the dog have other allergy-type symptoms?'
            ]),
            ('What to expect during elimination diet trials', 'An elimination diet is the most reliable way to test for food allergy in dogs.', [
                'Switch to a simple, novel protein diet',
                'Maintain the diet for several weeks to see improvement',
                'Avoid all treats and flavored chews during the trial',
                'Reintroduce ingredients slowly under vet guidance',
                'Watch closely for any return of skin symptoms',
                'Record every meal and symptom observation'
            ])
        ]
    },
    {
        'filename': 'dog-fungal-skin-infection-symptoms.html',
        'title': 'Dog Fungal Skin Infection Symptoms',
        'description': 'Detect dog fungal skin infection symptoms early and learn how veterinarians diagnose and treat these common conditions.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-fungal-skin-infection-symptoms.jpg',
        'sections': [
            ('What causes fungal skin infections?', 'Fungal infections thrive in moist, warm areas and often develop where the skin is already irritated.', [
                'Yeast overgrowth on the skin or in ears',
                'Tinea or ringworm infections',
                'Warm, damp skin folds',
                'Allergy-related skin breakdown',
                'Health conditions that weaken skin defenses',
                'Poor hygiene in high-risk areas'
            ]),
            ('Typical fungal infection signs', 'These infections often produce a mix of irritation, odor, and characteristic lesions.', [
                'Red, itchy patches with flaky skin',
                'A musty or unpleasant smell',
                'Greasy-looking coat or discharge',
                'Scaly, crusted spots',
                'May appear in overlapping, irregular shapes',
                'Discoloration in skin folds'
            ]),
            ('How fungal infections are diagnosed', 'Veterinarians use examination and tests to confirm a fungal cause and choose the right treatment.', [
                'Cytology with skin scrapings or swabs',
                'Microscopic examination for yeast or spores',
                'Fungal culture in uncertain cases',
                'Assessment of any underlying allergies',
                'Evaluation of skin moisture and hygiene habits',
                'Observation of response to initial therapy'
            ]),
            ('Treatment and management strategies', 'Treatment often includes topical therapy, oral medication, and preventive care to keep the skin healthy.', [
                'Medicated shampoos with antifungal ingredients',
                'Topical sprays or creams for localized spots',
                'Prescription oral antifungal drugs when needed',
                'Regular drying and cleaning of skin folds',
                'Treating any underlying triggers simultaneously',
                'Preventive care to avoid recurrence'
            ])
        ]
    },
    {
        'filename': 'dog-folliculitis-acne-symptoms-treatment.html',
        'title': 'Dog Folliculitis and Acne Symptoms Treatment',
        'description': 'Understand dog folliculitis and acne symptoms, treatment options, and how to keep your pet’s skin clear and comfortable.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-folliculitis-acne-symptoms-treatment.jpg',
        'sections': [
            ('What is canine folliculitis?', 'Folliculitis is inflammation of the hair follicle that often appears like pimples, bumps, or pustules on the skin.', [
                'Small red bumps around hair follicles',
                'Pustules that may ooze or dry',
                'Hair loss in the affected areas',
                'Crusts or scabs over irritated follicles',
                'Tenderness or discomfort when touched',
                'Follicular plugging with oil and debris'
            ]),
            ('Acne-like lesions in dogs', 'Dog acne often develops on the chin, lips, or chest and may look similar to human acne.', [
                'Blackheads or whiteheads on the chin',
                'Red, swollen spots on the face or neck',
                'Wax buildup around the mouth',
                'Greasy, irritated skin',
                'Pimples that become a secondary infection',
                'Localized discomfort during grooming'
            ]),
            ('Common causes of folliculitis and acne', 'Several factors can contribute to these skin problems, including poor hygiene and bacterial infection.', [
                'Bacterial overgrowth in the skin',
                'Blocked hair follicles from oil or debris',
                'Allergic skin inflammation',
                'Damage from scratching or rubbing',
                'Hormonal changes or stress',
                'Poor shaving or grooming practices'
            ]),
            ('Treatment options and home care', 'Treatment combines medical care with gentle at-home skin maintenance.', [
                'Antiseptic washes and medicated shampoos',
                'Topical therapies to calm the skin',
                'Oral antibiotics when infection develops',
                'Avoiding harsh products and excessive washing',
                'Keeping the area clean and dry',
                'Balancing treatment with comfort'
            ])
        ]
    },
    {
        'filename': 'dog-atopic-dermatitis-symptoms-lifestyle-care.html',
        'title': 'Dog Atopic Dermatitis Symptoms and Lifestyle Care',
        'description': 'Discover dog atopic dermatitis symptoms and lifestyle care strategies to help your dog manage chronic itchy skin effectively.',
        'image': 'https://mmm071026246-lgtm.github.io/images/dog-atopic-dermatitis-symptoms-lifestyle-care.jpg',
        'sections': [
            ('Recognizing atopic dermatitis', 'Atopic dermatitis is a chronic allergic skin condition that usually shows as ongoing itching and inflammation.', [
                'Recurring itchy patches on the face, paws, or belly',
                'Red, swollen skin that may become raw',
                'Chronic ear infections or head shaking',
                'Thickened skin from repeated scratching',
                'Seasonal flare-ups with pollen or dust',
                'Hot spots that return repeatedly'
            ]),
            ('How lifestyle affects atopic dermatitis', 'Daily routines, diet, and environment play a major role in controlling symptoms.', [
                'Regular bathing with a mild shampoo',
                'Consistent flea and parasite prevention',
                'Reducing exposure to known allergens',
                'Maintaining a clean living area',
                'Balanced nutrition to support skin health',
                'Stress reduction with predictable routines'
            ]),
            ('Key symptoms to monitor', 'Keeping track of specific symptoms helps your veterinarian adjust treatment over time.', [
                'Frequency and severity of itching',
                'Changes in skin texture or color',
                'Occurrence of secondary infections',
                'Response to medication or diet changes',
                'Any new triggers in the environment',
                'Seasonal or weather-related patterns'
            ]),
            ('Supportive care for long-term relief', 'Lifestyle care can improve comfort and reduce the number of flare-ups.', [
                'Use hypoallergenic bedding and cleaners',
                'Avoid frequent exposure to strong scents',
                'Offer omega fatty acid supplements if recommended',
                'Plan regular grooming and skin checks',
                'Keep stress low with predictable routines',
                'Work with your vet on a personalized care plan'
            ])
        ]
    }
]

base_style = '''body{font-family:Arial,sans-serif;max-width:920px;margin:0 auto;padding:24px;background:#ffffff;color:#1f2937;line-height:1.75;}
html{background:#f8fafc;}
a{color:#2563eb;text-decoration:none;}a:hover{text-decoration:underline;}
.breadcrumb{margin-bottom:24px;color:#6b7280;font-size:14px;}.breadcrumb a{color:#2563eb;}
h1{font-size:32px;margin-bottom:18px;}
h2{font-size:24px;margin-top:36px;margin-bottom:14px;}
h3{font-size:20px;margin-top:28px;margin-bottom:12px;}p{margin:16px 0;}ul{margin:16px 0 16px 24px;}li{margin:10px 0;}table{width:100%;border-collapse:collapse;margin:24px 0;}th,td{border:1px solid #d1d5db;padding:14px;vertical-align:top;}th{background:#eff6ff;}.notice{background:#eff6ff;border-left:4px solid #2563eb;padding:18px;margin:28px 0;border-radius:8px;}.ad-box{margin:34px 0;text-align:center;}.related-box{background:#f8fafc;padding:22px;border-radius:10px;margin-top:42px;}.related-box ul{margin:0;padding-left:20px;}.footer-note{color:#6b7280;font-size:14px;margin-top:42px;text-align:center;}
'''

opening_sections = [
    {
        'heading': 'Why early attention matters',
        'intro': 'Early attention to skin symptoms helps prevent minor issues from becoming chronic or painful.',
        'paragraphs': [
            'Skin irritation may look harmless at first, but it often reflects an underlying condition that needs care.',
            'The sooner you identify the cause, the faster your dog can receive targeted treatment.',
            'Delaying care can increase the risk of infection, secondary problems, and discomfort.'
        ]
    },
    {
        'heading': 'What sets skin problems apart',
        'intro': 'Not all skin problems are the same; some are seasonal, some are hereditary, and some are triggered by the environment.',
        'paragraphs': [
            'A careful observation of symptoms helps distinguish between allergies, infections, and irritation.',
            'Some dogs are sensitive to specific foods or topical products, while others react to pests or plants.',
            'Knowing the type of skin issue guides you to the right vet care and home support.'
        ]
    }
]

extra_sections = [
    {
        'heading': 'Breed and coat considerations',
        'intro': 'Different breeds and coat types can influence how skin symptoms appear and how they should be cared for.',
        'bullets': [
            'Brachycephalic breeds often have sensitive facial skin.',
            'Long-haired dogs can hide early signs until the condition worsens.',
            'Short-coated breeds may show redness and irritation more clearly.',
            'Double-coated dogs need careful grooming during hot weather.',
            'Curly-coated breeds can trap moisture and irritants near the skin.',
            'Hairless breeds require special topical protection.'
        ],
        'paragraphs': [
            'Adapting care to your dog’s coat type can prevent unnecessary irritation and help identify problems sooner.',
            'Regular grooming and inspection are especially important for breeds prone to skin issues.'
        ]
    },
    {
        'heading': 'Nutrition and skin health',
        'intro': 'The right nutrition supports a strong skin barrier and can reduce inflammation from allergens and irritants.',
        'bullets': [
            'Omega fatty acids help maintain healthy skin and coat.',
            'Quality protein supports healing and hair growth.',
            'Hydration is essential for supple skin.',
            'Avoid foods known to trigger allergies in your dog.',
            'Consider limited-ingredient diets when testing for reactions.',
            'Supplement carefully under veterinary guidance.'
        ],
        'paragraphs': [
            'A balanced diet is a foundation for healthy skin, and some dogs benefit from specially formulated allergy diets.',
            'Always introduce new foods gradually and keep detailed notes on any changes.'
        ]
    },
    {
        'heading': 'Daily care habits that help',
        'intro': 'Small daily habits can make a big difference in managing and preventing skin problems.',
        'bullets': [
            'Check the coat and skin regularly for new signs.',
            'Keep bedding clean to reduce allergens and irritants.',
            'Trim nails to prevent self-inflicted skin damage.',
            'Use gentle grooming tools that avoid further irritation.',
            'Provide a calm routine to reduce stress.',
            'Keep your dog well-hydrated at all times.'
        ],
        'paragraphs': [
            'Daily care does not require harsh treatments; consistency and attention are more important than aggressive products.',
            'Frequent checks let you detect changes quickly before they become more serious.'
        ]
    },
    {
        'heading': 'How to support recovery',
        'intro': 'Providing a supportive, low-stress environment is key to helping your dog recover from skin problems.',
        'bullets': [
            'Offer a quiet space to rest away from other pets.',
            'Keep the area clean and dry after bathing.',
            'Monitor for any signs of infection or worsening symptoms.',
            'Follow the veterinarian’s care plan closely.',
            'Avoid excessive handling if your dog is sensitive.',
            'Reintroduce activity slowly as symptoms improve.'
        ],
        'paragraphs': [
            'Recovery is a process, and your dog may need several days or weeks to fully improve depending on the condition.',
            'Gentle care and patience help prevent setbacks and support long-term wellness.'
        ]
    }
]

faq_items = [
    {
        'question': 'How do I know if my dog needs a vet for skin issues?',
        'answer': 'If skin symptoms are persistent, spreading, painful, or accompanied by other signs like fever, seek veterinary care promptly.'
    },
    {
        'question': 'Can I treat mild skin irritation at home?',
        'answer': 'Mild irritation may improve with gentle care, but consult your veterinarian before using treatments or assuming it will resolve on its own.'
    },
    {
        'question': 'How long does it take for skin symptoms to improve?',
        'answer': 'Improvement can vary from a few days to several weeks depending on the cause and the treatment plan.'
    }
]

related_links = [
    ('Dog Preventive Care Guide', 'dog-preventive-care-guide.html'),
    ('Annual Dog Wellness Exam', 'annual-dog-wellness-exam.html'),
    ('Dog Health Screening Guide', 'dog-health-screening-guide.html'),
    ('Dog Vaccine Side Effects', 'dog-vaccine-side-effects.html'),
    ('Dog First Aid Basics', 'dog-first-aid-basics.html')
]

for page in pages:
    path = Path('dog-blog/health') / page['filename']
    content = []
    content.append('<!DOCTYPE html>')
    content.append('<html lang="en">')
    content.append('<head>')
    content.append('<meta charset="UTF-8">')
    content.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    content.append(f'<title>{page["title"]} | Dog Health</title>')
    content.append(f'<meta name="description" content="{page["description"]}" />')
    content.append('<meta name="robots" content="index,follow,max-image-preview:large">')
    content.append(f'<link rel="canonical" href="https://mmm071026246-lgtm.github.io/dog-blog/health/{page["filename"]}">')
    content.append(f'<meta property="og:title" content="{page["title"]} | Dog Health">')
    content.append(f'<meta property="og:description" content="{page["description"]}">')
    content.append('<meta property="og:type" content="article">')
    content.append(f'<meta property="og:url" content="https://mmm071026246-lgtm.github.io/dog-blog/health/{page["filename"]}">')
    content.append('<meta property="og:site_name" content="Pet Calculators">')
    content.append('<meta property="og:locale" content="en_US">')
    content.append(f'<meta property="og:image" content="{page["image"]}">')
    content.append(f'<meta property="og:image:alt" content="{page["title"]} image">')
    content.append('<meta name="twitter:card" content="summary_large_image">')
    content.append(f'<meta name="twitter:title" content="{page["title"]} | Dog Health">')
    content.append(f'<meta name="twitter:description" content="{page["description"]}">')
    content.append(f'<meta name="twitter:image" content="{page["image"]}">')
    content.append('<meta name="theme-color" content="#2563eb">')
    content.append('')
    content.append('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9374368296307755" crossorigin="anonymous"></script>')
    content.append('')
    content.append('<script type="application/ld+json">')
    blog_posting = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": page['title'],
        "description": page['description'],
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://mmm071026246-lgtm.github.io/dog-blog/health/{page['filename']}"
        },
        "author": {
            "@type": "Organization",
            "name": "Pet Calculators"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Pet Calculators"
        },
        "image": page['image'],
        "articleSection": "Dog Health",
        "keywords": [
            page['title'].lower(),
            "canine health",
            "dog care",
            "dog skin symptoms",
            "dog health guide"
        ]
    }
    content.append(json.dumps(blog_posting, indent=2))
    content.append('</script>')
    content.append('')
    content.append('<script type="application/ld+json">')
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq_items[0]["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq_items[0]["answer"]
                }
            },
            {
                "@type": "Question",
                "name": faq_items[1]["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq_items[1]["answer"]
                }
            },
            {
                "@type": "Question",
                "name": faq_items[2]["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq_items[2]["answer"]
                }
            }
        ]
    }
    content.append(json.dumps(faq, indent=2))
    content.append('</script>')
    content.append('')
    content.append('<style>')
    content.append(base_style)
    content.append('</style>')
    content.append('</head>')
    content.append('<body>')
    content.append('')
    content.append('<nav class="breadcrumb" aria-label="breadcrumb">')
    content.append('    <a href="../index.html">Dog Health Hub</a> ›')
    content.append('    <a href="index.html">Health Guides</a> ›')
    content.append(f'    <span>{page["title"]}</span>')
    content.append('</nav>')
    content.append('')
    content.append(f'<h1>{page["title"]}</h1>')
    content.append('')
    content.append(f'<p>{page["description"]}</p>')
    content.append('')
    content.append(f'<p>{page["description"]} This article provides a detailed, practical guide to help you recognize symptoms, react wisely, and support your dog every step of the way.</p>')
    content.append('')
    content.append('<div class="notice">')
    content.append('    <strong>Key point:</strong> Early recognition and careful follow-up can make a big difference in how quickly your dog recovers from skin problems.')
    content.append('</div>')
    content.append('')
    content.append('<div class="ad-box">')
    content.append('    <ins class="adsbygoogle"')
    content.append('    style="display:block"')
    content.append('    data-ad-client="ca-pub-9374368296307755"')
    content.append('    data-ad-slot="8079351163"')
    content.append('    data-ad-format="auto"')
    content.append('    data-full-width-responsive="true"></ins>')
    content.append('    <script>')
    content.append('    (adsbygoogle = window.adsbygoogle || []).push({});')
    content.append('    </script>')
    content.append('</div>')
    content.append('')
    content.append('<p>This guide is designed for dog owners who want a clear, step-by-step understanding of symptoms and clinic-ready information to share with their veterinarian.</p>')
    content.append('<p>A proactive approach to skin care helps prevent minor issues from becoming painful or chronic.</p>')
    content.append('')

    for section in opening_sections:
        content.append(f'<h2>{section["heading"]}</h2>')
        content.append(f'<p>{section["intro"]}</p>')
        for paragraph in section['paragraphs']:
            content.append(f'<p>{paragraph}</p>')
        content.append('')

    for idx, (heading, intro, bullets) in enumerate(page['sections']):
        content.append(f'<h2>{heading}</h2>')
        content.append(f'<p>{intro}</p>')
        content.append('<ul>')
        for item in bullets:
            content.append(f'    <li>{item}</li>')
        content.append('</ul>')
        content.append('<h3>How this sign develops</h3>')
        content.append('<p>These are symptoms that may start slowly and become more obvious as the condition evolves.</p>')
        content.append('<p>It is important to monitor whether symptoms are isolated or part of a recurring pattern.</p>')
        content.append('<h3>What to do next</h3>')
        content.append('<p>When you notice these signs, consider both immediate comfort and whether veterinary evaluation is needed.</p>')
        content.append('<p>Keep a written record of the symptoms, their timing, and any related activity or exposures.</p>')
        content.append('<p>If the condition persists for more than a day or seems to worsen, schedule a vet visit.</p>')
        content.append('')
        if idx == 1:
            content.append('<div class="ad-box">')
            content.append('    <ins class="adsbygoogle"')
            content.append('    style="display:block"')
            content.append('    data-ad-client="ca-pub-9374368296307755"')
            content.append('    data-ad-slot="8079351163"')
            content.append('    data-ad-format="auto"')
            content.append('    data-full-width-responsive="true"></ins>')
            content.append('    <script>')
            content.append('    (adsbygoogle = window.adsbygoogle || []).push({});')
            content.append('    </script>')
            content.append('</div>')
            content.append('')

    content.append('<h2>Detailed symptom check table</h2>')
    content.append('<p>Use this table to rate the urgency of the symptoms you observe.</p>')
    content.append('<table>')
    content.append('    <thead>')
    content.append('        <tr>')
    content.append('            <th>Symptom</th>')
    content.append('            <th>Possible meaning</th>')
    content.append('            <th>Recommended action</th>')
    content.append('        </tr>')
    content.append('    </thead>')
    content.append('    <tbody>')
    content.append('        <tr>')
    content.append('            <td>Occasional scratching</td>')
    content.append('            <td>Often minor irritation or a brief reaction.</td>')
    content.append('            <td>Monitor and keep the area clean.</td>')
    content.append('        </tr>')
    content.append('        <tr>')
    content.append('            <td>Constant licking or chewing</td>')
    content.append('            <td>May indicate pain, itch, or an allergy.</td>')
    content.append('            <td>Check for wounds and consult your vet if persistent.</td>')
    content.append('        </tr>')
    content.append('        <tr>')
    content.append('            <td>Open sores or discharge</td>')
    content.append('            <td>Suggests infection or severe inflammation.</td>')
    content.append('            <td>Seek veterinary care promptly.</td>')
    content.append('        </tr>')
    content.append('    </tbody>')
    content.append('</table>')
    content.append('')

    content.append('<h2>Step-by-step action plan</h2>')
    content.append('<ol>')
    content.append('    <li>Observe the symptoms and note when they began.</li>')
    content.append('    <li>Check for external triggers like new food or plants.</li>')
    content.append('    <li>Manage immediate comfort with gentle care and a clean environment.</li>')
    content.append('    <li>If symptoms persist, photograph the affected area for better vet communication.</li>')
    content.append('    <li>Contact your veterinarian if the condition does not improve in 24-48 hours.</li>')
    content.append('    <li>Follow the treatment plan and keep all follow-up appointments.</li>')
    content.append('    <li>Monitor for improvement and any new symptoms during recovery.</li>')
    content.append('    <li>Adjust home care habits to prevent recurrence.</li>')
    content.append('</ol>')
    content.append('')

    for section in extra_sections:
        content.append(f'<h2>{section["heading"]}</h2>')
        content.append(f'<p>{section["intro"]}</p>')
        content.append('<ul>')
        for bullet in section['bullets']:
            content.append(f'    <li>{bullet}</li>')
        content.append('</ul>')
        for paragraph in section['paragraphs']:
            content.append(f'<p>{paragraph}</p>')
        content.append('')

    content.append('<h2>Frequently asked questions</h2>')
    for item in faq_items:
        content.append(f'<h3>{item["question"]}</h3>')
        content.append(f'<p>{item["answer"]}</p>')
    content.append('')

    content.append('<h2>Helpful resources</h2>')
    content.append('<p>Alongside this guide, these tools can help you keep your dog’s health and comfort on track.</p>')
    content.append('<ul>')
    content.append('    <li><a href="../../dog/dog-age-calculator.html">Dog Age Calculator</a> — Help match care to your dog’s life stage.</li>')
    content.append('    <li><a href="../../dog/dog-ideal-weight-calculator.html">Dog Ideal Weight Calculator</a> — Maintain healthy body condition during recovery.</li>')
    content.append('    <li><a href="../../dog/dog-water-intake-calculator.html">Dog Water Intake Calculator</a> — Keep hydration on track.</li>')
    content.append('    <li><a href="../../dog/dog-food-calculator.html">Dog Food Calculator</a> — Plan balanced nutrition for skin health.</li>')
    content.append('</ul>')
    content.append('')

    content.append('<div class="related-box">')
    content.append('    <h3>Related guides:</h3>')
    content.append('    <ul>')
    for title, href in related_links[:4]:
        content.append(f'        <li><a href="{href}">{title}</a></li>')
    content.append('    </ul>')
    content.append('</div>')
    content.append('')

    content.append('<h2>Final takeaways</h2>')
    content.append('<p>Skin problems are common, but prompt attention and consistent care can help your dog recover and stay comfortable.</p>')
    content.append('<p>Use this guide to observe symptoms carefully, support your dog at home, and communicate clearly with your veterinarian.</p>')
    content.append('')
    content.append('<footer class="footer-note">')
    content.append('    Pet Calculators © . Always consult a licensed veterinarian for personalized medical advice.')
    content.append('</footer>')
    content.append('')
    content.append('</body>')
    content.append('</html>')

    path.write_text('\n'.join(content), encoding='utf-8')
    print(f'Wrote {path.name} with {len(content)} lines')

print('\nVerification:')
for page in pages:
    path = Path('dog-blog/health') / page['filename']
    text = path.read_text(encoding='utf-8')
    print(path.name, 'lines=', len(text.splitlines()), 'ads=', text.count('data-ad-slot="8079351163"'))
