#include <bits/stdc++.h>

typedef long long ll;
#define trv(y,x) for(typeof(x.begin())y=x.begin();y!=x.end();y++)
using namespace std;

#define INF 1000000001
#define NMAX 1000
#define NIL 0
vector<int> Adj[NMAX];
int people[405][2], taxi[205][2];
int n,m;
int match[NMAX],dist[NMAX];



bool bfs()
{
    int i,u,v;
    queue<int> Q;
    for(i=1;i<=n;i++)
    {
        if(match[i]==NIL)
        {
            dist[i]=0;
            Q.push(i);
        }
        else dist[i]=INF;
    }
    dist[NIL]=INF;
    while(!Q.empty())
    {
        u=Q.front();
        Q.pop();
        if(u!=NIL)
        {
            trv(it,Adj[u])
            {
                v=(*it);
                if(dist[match[v]]==INF)
                {
                    dist[match[v]]=dist[u]+1;
                    Q.push(match[v]);
                }
            }
        }
    }
    return (dist[NIL]!=INF);
}

bool dfs(int u)
{
    int v;
    if(u!=NIL)
    {
        trv(it,Adj[u])
        {
            v=(*it);
            if(dist[match[v]]==dist[u]+1)
            {
                if(dfs(match[v]))
                {
                    match[v]=u;
                    match[u]=v;
                    return true;
                }
            }
        }
        dist[u]=INF;
        return false;
    }
    return true;
}

int HopcroftKarp()
{
    int matching=0,i;
    fill(match,match+n+m+1,NIL);
    while(bfs())
    {
        for(i=1;i<=n;i++)
        {
            if(match[i]==NIL && dfs(i))
                matching++;
        }
    }
    return matching;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int k,p,t,s,c,i,j,d;
    cin>>k;
    while(k--)
    {
        cin>>p>>t>>s>>c;
        n=p; m=t;
        for(i=0;i<p;i++) cin>>people[i][0]>>people[i][1];
        for(i=0;i<t;i++) cin>>taxi[i][0]>>taxi[i][1];
        d=s*c;
        for(i=0;i<p;i++)
        {
            for(j=0;j<t;j++)
            {
                if(200*(abs(people[i][0]-taxi[j][0])+abs(people[i][1]-taxi[j][1]))<=d)
                {
                    Adj[i+1].push_back(n+j+1);
                    Adj[n+j+1].push_back(i+1);
                }
            }
        }

        cout<<HopcroftKarp()<<"\n";
        for(i=0;i<=(n+m);i++) Adj[i].clear();
    }
    return 0;
}