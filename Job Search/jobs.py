import webbrowser
import sys

sites = [
    'https://stackoverflow.com/jobs?l=India&d=20&u=Km&tl=django+flask+bootstrap-4+python-3.x+mongodb+sql+javascript+html+css&dr=BackendDeveloper&dr=FrontendDeveloper&dr=FullStackDeveloper',
    'https://internshala.com/fresher-jobs/computer%20science,python%2Fdjango,web%20development-fresher-job',
    'https://startup.jobs/?query=python&places%5Bquery%5D%5B0%5D=India&places%5Bposition%5D=20.5937%2C78.9629',
    'https://weworkremotely.com/remote-jobs/search?term=python&button=&categories%5B%5D=2&region%5B%5D=Anywhere+%28100%25+Remote%29+Only'
    'https://remoteok.io/remote-python-jobs',
    'https://cutshort.io/profile/search/jobs/q?expRange=0-1&minexp=0&maxexp=1&skills=00360&matchesfor=602b44c326cb020b512e4b57',
    'https://www.linkedin.com/jobs/search/?f_E=2&f_F=eng%2Cit&f_I=96%2C4&f_JT=F%2CI&f_L=India&geoId=102713980&keywords=python%20developer&location=India&sortBy=R',
    'https://www.naukri.com/python-jobs?industryTypeId=25&experience=0',
    'https://angel.co/jobs?ref=onboarding#',
    'https://internshala.com/internships/python%2Fdjango-internship',
    'https://www.capgemini.com/in-en/careers/job-search/?search_term=python',
    'https://www.codechef.com/careers',
    'https://practice.geeksforgeeks.org/jobs/',
    'https://www.geeksforgeeks.org/careers/?',
    'https://internshala.com/careers',
]

dream = [
    'https://careers.microsoft.com/students/us/en/ur-lp-india',
    'https://about.instagram.com/about-us/careers',
    'https://github.com/about/careers',
    'https://www.facebook.com/careers/jobs/?offices%5B0%5D=Mumbai%2C+India&offices%5B1%5D=New+Delhi%2C+India&offices%5B2%5D=Hyderabad%2C+India&offices%5B3%5D=Bangalore%2C+India&offices%5B4%5D=Gurgaon%2C+India&is_leadership=0&teams%5B0%5D=Internship+-+Engineering%2C+Tech+%26+Design&teams%5B1%5D=Software+Engineering&teams%5B2%5D=University+Grad+-+Engineering%2C+Tech+%26+Design&is_in_page=0',
    'https://www.amazon.jobs/en-gb/teams/internships-for-students?offset=0&result_limit=10&sort=recent&category[]=software-development&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&',
    'https://www.amazon.jobs/en-gb/teams/jobs-for-grads?offset=0&result_limit=10&sort=recent&category[]=software-development&cities[]=Bengaluru%2C%20Karnataka%2C%20IND&cities[]=Hyderabad%2C%20Telangana%2C%20IND&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&',
    'https://careers.google.com/jobs/results/?category=SOFTWARE_ENGINEERING&company=Google&company=YouTube&employment_type=FULL_TIME&employment_type=PART_TIME&employment_type=TEMPORARY&jex=ENTRY_LEVEL&jlo=en_US',
    'https://careers.google.com/jobs/results/?company=Google&company=YouTube&employment_type=INTERN&jlo=en_US&q=Software%20Engineer',
    'https://www.dropbox.com/jobs/all-jobs',
    'https://www.redditinc.com/careers#job-info',
    'https://discord.com/jobs?team=engineering',
    'https://www.goldmansachs.com/careers/students/programs/index.html'
]

for i in sites:
    webbrowser.open(i)
